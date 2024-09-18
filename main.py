from connectuser import Ui_MainWindow as uiUseS
from registerscreen import Ui_MainWindow as uiRegS
from passreplacescreen import Ui_Form as uiPasS
from menuscreen import Ui_MainWindow as uiMenuS
from PyQt5.QtCore import QProcess
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QVBoxLayout, QSizePolicy
from PyQt5 import QtWidgets, QtGui
from matplotlib.figure import Figure
from functions import *
from api_isbn import set_isbn
import pandas as pd
import webbrowser
import sys
class LoginScreen(QtWidgets.QMainWindow, uiUseS):
    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('LIBRYNO - Login')
        self.register_screen = None
        self.replacePass_screen = None
        self.home_screen = None
        self.buttonEnt.clicked.connect(self._button_enter)
        self.buttonCad.clicked.connect(self._window_register)
        self.pass_replace.clicked.connect(self._window_replace_pass)
    
    def _button_enter(self):
        nomeUser, senhaUser = self._valueLogin()
        if not (nomeUser and senhaUser):
            self._show_message('Campos Vazios', 'Os campos deverão ser preenchidos', QMessageBox.Warning)
            return
        instance_connect_login = LoginColab._login(nomeUser, senhaUser)
        if instance_connect_login:
            self._show_message('Sucesso', f'Login realizado com sucesso!\n\nSeja bem-vindo {nomeUser}', QMessageBox.Information)
            if self.home_screen is None:
                self.home_screen = HomeScreen(self)
            self.home_screen.show()
            self.hide()
        elif instance_connect_login is False:
            self._show_message('Problemas com o Usuário', 'Usuário ou senha estão errados', QMessageBox.Critical)
            
    def _window_register(self):
        if self.register_screen is None:  
            self.register_screen = RegisterScreen(self)
        self.register_screen.show()
        self.hide()

    def _window_replace_pass(self):
        if self.replacePass_screen is None:  
            self.replacePass_screen = ReplacePassScreen(self)
        self.replacePass_screen.show()
        self.hide()

    def _valueLogin(self):
        return self.inputUser.text(), self.inputPass.text()

    def _show_message(self, title, message, icon):
        boxMessage(title=title, message=message, button=QMessageBox.Ok, icon=icon)
class ReplacePassScreen(QtWidgets.QWidget, uiPasS):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle('LIBRYNO - Mudar Senha')
        self.button_return.clicked.connect(self._button_return_Pass)
        self.button_save.clicked.connect(self._saveDateUser)
        
    def _saveDateUser(self):
        rpuser, rpsenha, rpsenhaC = self._value_input_RP()
        if not (rpuser and rpsenha):
            self.parent._show_message('Campos Vazios', 'Os campos deverão ser preenchidos', QMessageBox.Warning)
            return
        elif rpsenha != rpsenhaC:
            self.parent._show_message('Problema com a senha', 'As senhas devem ser iguais', QMessageBox.Warning)
            return
        
        instance_connect_login = LoginColab._replacePassword(rpuser, rpsenha)
        if instance_connect_login is None:
            self._button_return_Pass()

    def _value_input_RP(self):
        return self.inputUser_3.text(), self.inputPass_3.text(), self.inputPass_4.text()

    def _button_return_Pass(self):
        clear_line_edits(self,widget_type=QtWidgets.QLineEdit)
        self.close()
        if self.parent:
            self.parent.show()
class RegisterScreen(QtWidgets.QMainWindow, uiRegS):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle('LIBRYNO - Registro')
        self.button_registrar.clicked.connect(self._button_registrar)
        self.button_voltar.clicked.connect(self._button_voltar)
        self.pushButton_LGPD.clicked.connect(lambda: webbrowser.open('https://www.gov.br/mds/pt-br/acesso-a-informacao/governanca/integridade/campanhas/lgpd'))
        
    def _button_registrar(self):  
        try:
            rnome, rnomeUsuario, rsenha, rsenhaC = self._value_input_R()
            if not (rnome and rnomeUsuario and rsenha and rsenhaC):
                self.parent._show_message('Formulario incompleto', 'Todos os campos precisam estar preenchidos', QMessageBox.Warning)
                return
            elif len(rnome) < 3:
                self.parent._show_message('Problema com o nome', 'O nome tem que ter no mínimo 3 caracteres', QMessageBox.Warning)
                return
            elif len(rnomeUsuario) < 3:
                self.parent._show_message('Problema com o usuário', 'O usuário tem que ter no mínimo 3 caracteres', QMessageBox.Warning)
                return
            elif len(rsenha) < 5:
                self.parent._show_message('Problema com a senha', 'A senha deve ter no mínimo 5 caracteres', QMessageBox.Warning)
                return
            elif rsenha != rsenhaC:
                self.parent._show_message('Problema com a senha', 'As senhas devem ser iguais', QMessageBox.Warning)
                return
            
            self.new_colab = CrudColab.Criar_colab(rnome, rnomeUsuario, rsenha)            
            if self.new_colab is None:
                self._button_voltar()
        except AttributeError as e:
            print(f'Erro na configuração do botão: {e}')

    def _value_input_R(self):
        return self.input_nome.text(), self.input_novousuario.text(), self.input_novasenha.text(), self.input_confirmasenha.text()

    def _button_voltar(self):
        clear_line_edits(self,widget_type=QtWidgets.QLineEdit)
        self.close()
        if self.parent:
            self.parent.show()
class HomeScreen(QtWidgets.QMainWindow, uiMenuS):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle('LIBRYNO - Home')
        self._navPagIndex(index=0)
        self.widget.setVisible(False)
        self.pushButton_home.setChecked(True)
        self.pushButton_Menu.setChecked(True)
        self.register_screen = None
        self.replacePass_screen = None
        self._connect_buttons()
        self.lineEdit_ISBM_B.editingFinished.connect(self._consult_api_isbn)
        self.autenticado = False
        self._view_data_analitycs()
        self.plot_all()
    def _connect_buttons(self):
        self.pushButton_home.clicked.connect(lambda:self._navPagIndex(index=0))
        self.pushButton_home2.clicked.connect(lambda:self._navPagIndex(index=0))
        self.pushButton_on.clicked.connect(lambda:self._navPagIndex(index=4))
        self.pushButton_on2.clicked.connect(lambda:self._navPagIndex(index=4))
        self.pushButton_lib.clicked.connect(self._viewPageBook)
        self.pushButton_lib2.clicked.connect(self._viewPageBook)
        self.pushButton_reader.clicked.connect(self._viewPageReader)
        self.pushButton_reader2.clicked.connect(self._viewPageReader)
        self.pushButton_colab.clicked.connect(self._viewPageColab)
        self.pushButton_colab2.clicked.connect(self._viewPageColab)
        self.pushButton_Cad_B_Page.clicked.connect(self._tab_book_and_clear)
        self.pushButton_Cancel_B.clicked.connect(self._viewPageBook)
        self.pushButton_Cad_Reader_Page.clicked.connect(self._tab_reader_and_clear)
        self.pushButton_Cancel_Reader.clicked.connect(self._viewPageBook)
        self.pushButton_Cad_B.clicked.connect(self._cadBook)
        self.pushButton_Cad_Reader.clicked.connect(self._cadReader)
        self.pushButton_ReturnConnect.clicked.connect(self._return_Login)
        self.pushButton_Return_Connect2.clicked.connect(self._return_Login)
        self.pushButton_Cad_Colab_Page.clicked.connect(self._screen_Cad_Colab)
        self.pushButton_Refresh_Colab.clicked.connect(self._viewTableColab)
        self.pushButton_Refresh_Reader.clicked.connect(self._viewTableReader)
        self.pushButton_Refresh_B.clicked.connect(self._viewTableBook)
        self.pushButton_Not_Cep.clicked.connect(lambda: webbrowser.open('https://buscacepinter.correios.com.br/app/endereco/index.php'))
        self.pushButton_Update_Colab.clicked.connect(lambda: self._modify_update_table(CrudColab.Atualizar_colab, self.tableWidget_Colab))
        self.pushButton_Update_Reader.clicked.connect(lambda: self._modify_update_table(CrudLeitor.Atualizar_leitor, self.tableWidget_Reader))
        self.pushButton_Update_B.clicked.connect(lambda: self._modify_update_table(CrudLivros.Atualizar_livro, self.tableWidget_B))
        self.pushButton_Delete_Colab.clicked.connect(lambda: self._modify_delete_table(CrudColab.Deletar_colab, self.tableWidget_Colab))
        self.pushButton_Delete_Reader.clicked.connect(lambda: self._modify_delete_table(CrudLeitor.Deletar_leitor, self.tableWidget_Reader))
        self.pushButton_Delete_B.clicked.connect(lambda: self._modify_delete_table(CrudLivros.Deletar_livro, self.tableWidget_B))
        self.pushButton_Export_Excel_B.clicked.connect(lambda:self._createExcel(tableB=True))
        self.pushButton_Export_Excel_Reader.clicked.connect(lambda:self._createExcel(tableR=True))
        self.pushButton_Seach_Home.clicked.connect(self._seach_table)
    def _navPagIndex(self,index=None):
        if index is not None:
            self.stackedWidget.setCurrentIndex(index)
        if index == 0:
            self._view_data_analitycs()
            self.plot_all()
    def _viewPageBook(self):
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self._viewTableBook()
    def _viewPageReader(self):
        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        self._viewTableReader()
    def _viewPageColab(self):
        self.stackedWidget.setCurrentIndex(3)
        self._viewTableColab()
    def _tab_reader_and_clear(self):
        self.tabWidget.setCurrentIndex(1)
        clear_line_edits(self,widget_type=QtWidgets.QLineEdit)
    def _tab_book_and_clear(self):
        self.tabWidget_2.setCurrentIndex(1)
        clear_line_edits(self,widget_type=QtWidgets.QLineEdit)
        clear_line_edits(self,widget_type=QtWidgets.QTextEdit)
    def _viewTableColab(self):
        if self.autenticado :
            self._loading_table_colab()
            return
        elif self.autenticado == False:    
            msg_show_colab_pass = self._show_message('Alerta','Area sensivel, ao entrar nessa area voce precisará de uma senha, para visualização das senhas dos colaboradores',QMessageBox.Critical)
            if msg_show_colab_pass == True:
                self._solicitar_senha()
            else:
                self._show_message('Botão não clicado', 'Click no botão para continuar', QMessageBox.Critical)
    def _viewTableReader(self):
        record = CrudLeitor.Ler_leitor()
        self.tableWidget_Reader.setRowCount(len(record))
        for row_index, row_data in enumerate(record):
            for column_index, column_data in enumerate(row_data):
                self.tableWidget_Reader.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(column_data)))
    def _viewTableBook(self):
        record = CrudLivros.Ler_livro()
        self.tableWidget_B.setRowCount(len(record))
        self.tableWidget_B.setColumnCount(len(record[0]) if record else 0)
        for row_index,row_data in enumerate(record):
            for column_index,column_data in enumerate(row_data):
                self.tableWidget_B.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(column_data)))
    def _screen_Cad_Colab(self):
        if self.register_screen is None:  
            self.register_colab_screen = RegisterScreen(self)
        self.register_colab_screen.show()
        self.close()  
    def _modify_update_table(self, update_function=None, table=None):
        try:
            upDate = []
            for row in range(table.rowCount()):
                dados = []
                for column in range(table.columnCount()):
                    item = table.item(row, column)
                    if item is not None:
                        dados.append(item.text().strip())
                    else:
                        dados.append('')
                
                if dados:
                    upDate.append(dados)
            print("Dados a atualizar:", upDate)

            if not upDate:
                self._show_message('Nenhum campo mudado', 'Não tem dados para atualizar', QMessageBox.Information)
                return
            for Data in upDate:
                update_function(tuple(Data))
            if Data:
                self._show_message('Sucesso', 'Os dados foram atualizados com sucesso', QMessageBox.Information)
            
        except psycopg2.IntegrityError as ie:
            self._show_message('Erro', f'Erro na integridade dos dados, os dados não foram atualizados\nErro: {ie}', QMessageBox.Information)
            
        except Exception as e:
            self._show_message('Erro', f'Erro de conexão com o banco, os dados não foram atualizados\nErro: {e}', QMessageBox.Information)        
    def _modify_delete_table(self,met,table): 
        selected_row = table.currentRow()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Os dados que você selecionou estão prestes a serem EXCLUÍDOS.\nVocê realmente deseja excluir os dados?")
        msg.setWindowTitle("Confirmação de exclusão")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = msg.exec()  
        if result == QMessageBox.Yes:
            if selected_row >= 0:
                row_id_item = table.item(selected_row, 0)
                if row_id_item:
                    row_id = row_id_item.text()
                    met(row_id)
                    table.removeRow(selected_row)
                    self.update()
    def _return_Login(self):
        QtWidgets.QApplication.quit()
        QProcess.startDetached(sys.executable, sys.argv)   
    def _cadReader(self):
        Name_Reader,Tel_Reader,Email_Reader,CPF_Reader,Ide_Reader,CEP_Reader,Sc_Reader,Dn_Reader,Address_Reader,D_Cad_Reader = self._value_input_Reader()
        try:
            if not (Name_Reader and CPF_Reader and Ide_Reader and D_Cad_Reader):
                self._show_message('Campos Importante','Os campos : \n\n Nome \n CPF \n Identidade \n Data de Cadastro, \n\n Deverão ser preenchidos!!!', QMessageBox.Warning)
                return
            if not (Tel_Reader and Email_Reader and CEP_Reader and Sc_Reader and Dn_Reader and Address_Reader):
                self._show_message('Campos Vazios','Os campos deverão ser preenchidos', QMessageBox.Warning)
                return
            
            self.cadReader = CrudLeitor.Criar_leitor(Name_Reader,Tel_Reader,Email_Reader,CPF_Reader,Ide_Reader,CEP_Reader,Sc_Reader,Dn_Reader,Address_Reader,D_Cad_Reader)
            if self.cadReader is None:
                clear_line_edits(self,widget_type=QtWidgets.QLineEdit)
        except Exception as e:
            print(f'problemas ao enviar os dados {e}')           
    def _cadBook(self):
        Num_Tombo_B,ISBn_B,Publisher_B,Year_E_B,Class_B,Num_Sheets_B,Title_B,Nome_Author,Volume_B,Date_Cad_B,Details_B = self._value_input_Book()
        if not (Num_Tombo_B and ISBn_B and Title_B and Date_Cad_B):
            self._show_message('Campos Importante','Os campos : \n\n Nº TOMBO \n ISBM \n Título do Livro \n Data de Cadastro, \n\n Deverão ser preenchidos!!!', QMessageBox.Warning)
            return
        if not (Publisher_B and Year_E_B and Num_Sheets_B and Nome_Author and Volume_B and Details_B):
            self._show_message('Campos Vazios','Os campos deverão ser preenchidos', QMessageBox.Warning)
            return
        self.cadBook = CrudLivros.Criar_livro(Num_Tombo_B,ISBn_B,Publisher_B,Year_E_B,Class_B,Num_Sheets_B,Title_B,Nome_Author,Volume_B,Date_Cad_B,Details_B)
        if self.cadBook is None:
            clear_line_edits(self,widget_type=QtWidgets.QLineEdit)
            clear_line_edits(self,widget_type=QtWidgets.QTextEdit)
    def _value_input_Reader(self):
        return (self.lineEdit_Name_Reader.text(),
                self.lineEdit_Tel_Reader.text(),
                self.lineEdit_Email_Reader.text(),
                self.lineEdit_CPF_Reader.text(),
                self.lineEdit_Ide_Reader.text(),
                self.lineEdit_CEP_Reader.text(),
                self.combo_Sc_Reader.currentText(),
                self.lineEdit_Dn_Reader.text(),
                self.lineEdit_Address_Reader.text(),
                self.lineEdit_D_Cad_Reader.text())
    def _value_input_Book(self):
        validator_large_int = QtGui.QIntValidator(0, 2147483647)
        validator_year = QtGui.QIntValidator(0, 9999)
        validator_small_int = QtGui.QIntValidator(0, 99999)
        id_validator = QtGui.QIntValidator(0, 999999999)
        self.lineEdit_Num_Tombo_B.setValidator(validator_large_int)
        self.lineEdit_Num_Tombo_B.setMaxLength(10) 
        self.lineEdit_ISBM_B.setValidator(validator_large_int)
        self.lineEdit_ISBM_B.setMaxLength(15) 
        self.lineEdit_Year_E_B.setValidator(validator_year)
        self.lineEdit_Year_E_B.setMaxLength(4)
        self.lineEdit_Volume_B.setValidator(validator_small_int)
        self.lineEdit_Volume_B.setMaxLength(5)
        self.lineEdit_Num_Sheets_B.setValidator(validator_large_int)
        self.lineEdit_Num_Sheets_B.setMaxLength(10)
        self.lineEdit_Ide_Reader.setValidator(id_validator)
        self.lineEdit_Ide_Reader.setMaxLength(10)
        self.lineEdit_Address_Reader.setMaxLength(100)
        return (self.lineEdit_Num_Tombo_B.text(),
                self.lineEdit_ISBM_B.text(),
                self.lineEdit_Publisher_B.text(),
                self.lineEdit_Year_E_B.text(),
                self.lineEdit_Class_B.text(),
                self.lineEdit_Num_Sheets_B.text(),
                self.lineEdit_Title_B.text(),
                self.lineEdit_Name_A_B.text(),
                self.lineEdit_Volume_B.text(),
                self.lineEdit_D_Cad_B.text(),
                self.textEdit_Details_B.toPlainText())
    def _consult_api_isbn(self):
        campo = set_isbn(self.lineEdit_ISBM_B.text())
        titleandsubtitle = f"{campo[0]} - {(campo[1])}"
        self.lineEdit_Title_B.setText(titleandsubtitle)
        self.lineEdit_Name_A_B.setText(", ".join(campo[2]))
        self.lineEdit_Publisher_B.setText(campo[3])
        self.textEdit_Details_B.setText(campo[4])
        self.lineEdit_Num_Sheets_B.setText(str(campo[5]))
    def _solicitar_senha(self):
        if self.autenticado:
            self._loading_table_colab()
            return
        senha, ok = QtWidgets.QInputDialog.getText(
        self, 'Verificação de Senha','Digite a senha para acessar a tabela:', echo=QtWidgets.QLineEdit.Password)
        
        if ok and senha == 'admin':  
            self.autenticado = True
            return self._loading_table_colab()
        if not ok:
            QMessageBox.information(self, 'Operação cancelada', 'Retorno ao home.')
            return self._navPagIndex(index=0)
        else:
            QMessageBox.warning(self, 'Erro', 'Senha incorreta. Acesso negado.')
            return self._solicitar_senha()  
    def _loading_table_colab(self):
        record = CrudColab.Ler_colab()
        self.tableWidget_Colab.clearContents()
        self.tableWidget_Colab.setRowCount(len(record))
        for row_index, row_data in enumerate(record):
            for column_index, column_data in enumerate(row_data):
                self.tableWidget_Colab.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(column_data)))
    def _show_message(self,title,message,icon):
        boxMessage(title=title, message=message,button=QMessageBox.Ok,icon=icon)
        return True
    def _createExcel(self, tableB=False, tableR=False):
        conn = None
        cursor = None
        try:
            conn = Conectar()
            if conn is None:
                self._show_message('Erro', 'Falha na conexão com o banco de dados', QMessageBox.Critical)
                return

            cursor = conn.cursor()
            if tableB:
                cursor.execute('SELECT * FROM public."Livros"')
                data = cursor.fetchall()

                if data:
                    file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Salvar arquivo Excel", "", "Excel Files (*.xlsx)")

                    if file_path:
                        df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
                        df.to_excel(f'{file_path}', sheet_name='Tabela_Livros', index=False)
                        self._show_message('Relatório salvo com sucesso', f'Sua planilha Livros foi criada em: {file_path}', QMessageBox.Information)
                    else:
                        self._show_message('Aviso', 'Nenhum local foi selecionado para salvar o arquivo.', QMessageBox.Warning)
                else:
                    self._show_message('Aviso', 'Nenhum dado encontrado na tabela Livros', QMessageBox.Warning)

            if tableR:
                cursor.execute('SELECT * FROM public."Leitor"')
                data = cursor.fetchall()

                if data:
                    file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Salvar arquivo Excel", "", "Excel Files (*.xlsx)")

                    if file_path:
                        df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
                        df.to_excel(f'{file_path}', sheet_name='Tabela_Leitor', index=False)
                        self._show_message('Relatório salvo com sucesso', f'Sua planilha Leitor foi criada em: {file_path}', QMessageBox.Information)
                    else:
                        self._show_message('Aviso', 'Nenhum local foi selecionado para salvar o arquivo.', QMessageBox.Warning)
                else:
                    self._show_message('Aviso', 'Nenhum dado encontrado na tabela Leitor', QMessageBox.Warning)

        except Exception as e:
            self._show_message('Erro', f'Erro ao gerar o relatório: {e}', QMessageBox.Critical)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
    def _seach_table(self):
        termo_pesquisa = self.input_Seach_Home.text().strip()  
        if not termo_pesquisa:
            self._show_message('Aviso', 'Por favor, digite um nome para pesquisar.', QMessageBox.Warning)
            return
        try:
            conn = Conectar()
            cursor = conn.cursor()
            
            queries_livros = {
                'titulo': 'SELECT * FROM public."Livros" WHERE titulo_livro ILIKE %s',
                'autor': 'SELECT * FROM public."Livros" WHERE autor ILIKE %s',
                'classificacao': 'SELECT * FROM public."Livros" WHERE classificacao ILIKE %s',
                'isbn': 'SELECT * FROM public."Livros" WHERE isbn ILIKE %s',
                'n_tombo': 'SELECT * FROM public."Livros" WHERE n_tombo ILIKE %s'
            }

            for key, query in queries_livros.items():
                cursor.execute(query, (f"%{termo_pesquisa}%",))
                resultado_livro = cursor.fetchone()
                if resultado_livro:
                    self.stackedWidget.setCurrentWidget(self.page_Lib)
                    self._selecionar_item_na_tabela(self.tableWidget_B, resultado_livro[0])
                    break
            else:
                queries_leitores = {
                    'nome': 'SELECT * FROM public."Leitor" WHERE nome ILIKE %s',
                    'cpf': 'SELECT * FROM public."Leitor" WHERE cpf ILIKE %s'
                }
                for key, query in queries_leitores.items():
                    cursor.execute(query, (f"%{termo_pesquisa}%",))
                    resultado_leitor = cursor.fetchone()
                    if resultado_leitor:
                        self.stackedWidget.setCurrentWidget(self.page_Reader)
                        self._selecionar_item_na_tabela(self.tableWidget_Reader, resultado_leitor[0])
                        break
                else:
                    self._show_message('Aviso', 'Nenhum item encontrado com esse nome.', QMessageBox.Warning)

        except Exception as e:
            self._show_message('Erro', f'Erro ao pesquisar: {e}', QMessageBox.Critical)

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def _selecionar_item_na_tabela(self, table, item_id):
        for row in range(table.rowCount()):
            item = table.item(row, 0)  
            if item and int(item.text()) == item_id:
                table.selectRow(row) 
                table.scrollToItem(item) 
                break
                from PyQt5.QtWidgets import QVBoxLayout
    def _view_data_analitycs(self):
        conn = Conectar() 
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM public."Livros"')
            result = cursor.fetchall()
            colunasR1 = [desc[0] for desc in cursor.description]
            df = pd.DataFrame(result, columns=colunasR1)
            cursor.execute('SELECT * FROM public."Leitor"')
            resultTwo = cursor.fetchall()
            colunasR2 = [desc[0] for desc in cursor.description]
            df2 = pd.DataFrame(resultTwo, columns=colunasR2)
            cursor.execute('SELECT * FROM public."Colab"')
            resultThree = cursor.fetchall()
            colunasR3 = [desc[0] for desc in cursor.description]
            df3 = pd.DataFrame(resultThree, columns=colunasR3)
        finally:
            cursor.close()
            conn.close()
        self.qtdVarB = df['id_livro'].count()
        self.anoEdicaoB = df['ano_edicao'].tolist()
        self.anoEdicaoB_count = df['ano_edicao'].value_counts()
        self.dataCadB = df['data_cadastro'].tolist()
        self.dataCadB_count = df['data_cadastro'].value_counts()
        self.qtdVarL = df2['id_leitor'].count()
        self.schoolL = df2['escolaridade'].tolist()
        self.schoolL_count = df2['escolaridade'].value_counts()
        self.dataCadL = df2['data_cadastro'].tolist()
        self.dataCadL_count = df2['data_cadastro'].value_counts()
        self.qtdVarC = df3['id_colab'].count()
        self.lPie = [self.qtdVarB, self.qtdVarC, self.qtdVarL]
    def pie(self, data, frame):
        fig = Figure(figsize=(2,2))
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111, aspect='equal')
        labels = ['Livros', 'Colaboradores', 'Leitores']
        ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
        fig.tight_layout()
        fig.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)  
        if frame.layout() is None:
            layout = QVBoxLayout()
            layout.setContentsMargins(1, 1, 1, 1)  
            layout.setSpacing(0) 
            frame.setLayout(layout)
        self.clear_frame(frame)
        frame.layout().addWidget(canvas)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.updateGeometry()  
    def bar(self, x, y, labely, labelx, title, frame):
        fig = Figure(figsize=(2,2))
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.bar(x, y)
        ax.set_ylabel(labely, fontsize=8)
        ax.set_xlabel(labelx, fontsize=8)
        ax.set_title(title, fontsize=10)
        fig.subplots_adjust(left=0.2, right=0.9, top=0.8, bottom=0.3)  
        if frame.layout() is None:
            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)  
            layout.setSpacing(0)  
            frame.setLayout(layout)
        self.clear_frame(frame)
        frame.layout().addWidget(canvas)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.updateGeometry()  
    def line(self, x, y, title, frame):
        fig = Figure(figsize=(2,2))
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.plot(x, y)
        ax.set_title(title, fontsize=10)
        fig.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.3)  
        if frame.layout() is None:
            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)  
            layout.setSpacing(0)  
            frame.setLayout(layout)
        self.clear_frame(frame)
        frame.layout().addWidget(canvas)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.updateGeometry() 
    def clear_frame(self, frame):
        layout = frame.layout()
        if layout:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()
    def plot_all(self):
        self.bar(
            x=list(self.anoEdicaoB_count.index),  
            y=self.anoEdicaoB_count.values,       
            labely='Quantidade de Livros',
            labelx='Ano de Edição',
            title='Livros pelo Ano de Edição',
            frame=self.frameG1
        )
        self.line(
            x=list(self.dataCadB_count.index),    
            y=self.dataCadB_count.values,         
            title='Livros pela Data de Cadastro',
            frame=self.frameG2
        )
        self.bar(
            x=list(self.schoolL_count.index),     
            y=self.schoolL_count.values,          
            labely='Quantidade de Leitores',
            labelx='Escolaridade',
            title='Escolaridade dos Leitores',
            frame=self.frameG3
        )
        self.line(
            x=list(self.dataCadL_count.index),    
            y=self.dataCadL_count.values,         
            title='Leitores pela Data de Cadastro',
            frame=self.frameG4
        )
        self.pie(
            data=self.lPie,
            frame=self.frameG5
        )
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('./img/icon.png'))
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())