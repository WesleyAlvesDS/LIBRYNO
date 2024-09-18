import psycopg2 
from PyQt5.QtWidgets import QMessageBox
def Conectar():
        try:
            
            conexao = psycopg2.connect(
                                host = 'localhost',
                                password = 'root',
                                port = '5432',
                                user = 'postgres', 
                                dbname = 'biblioteca_pm')
            print('Banco de dados conectado',conexao.info)   
            return conexao  
        except Exception as e:
            print(f'Banco de dados não conectado',{e})
            return None
def boxMessage(title,message,button,icon):
    boxAlert = QMessageBox()
    boxAlert.setIcon(icon)
    boxAlert.setWindowTitle(title)
    boxAlert.setText(message)
    boxAlert.setStandardButtons(button)
    boxAlert.exec()
def clear_line_edits(self, widget_type):
        for widget in self.findChildren(widget_type):
            widget.clear()
class LoginColab():
    @staticmethod
    def _login(nome_usuario,senha):
        conn = None
        cursor = None
        try:
            conn = Conectar()
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM public."Colab" WHERE nome_usuario = %s AND senha = %s', (nome_usuario, senha))
                result = cursor.fetchone()
                return result is not None              
        except Exception as e :
            boxMessage(title='Cadastro negado',message=f'Erro ao enviar os dados\n\nProblemas com o banco de dados\nErro : {e}',button=QMessageBox.Ok,icon=QMessageBox.Critical)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
    def _replacePassword(nome_usuario,senha):
        conn = None
        cursor = None
        try:
            conn = Conectar()
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM public."Colab" WHERE nome_usuario = %s', (nome_usuario,))
                result = cursor.fetchone()
                if result is not None:
                    cursor.execute('UPDATE public."Colab" SET senha = %s WHERE nome_usuario = %s', (senha, nome_usuario))
                    conn.commit()
                    boxMessage(title='Sucesso', message=f'Senha atualizada com sucesso!\n\nSeja bem vindo : {nome_usuario}', button=QMessageBox.Ok, icon=QMessageBox.Information)     
            else:
                boxMessage(title='Atualização negada', message=f'O usuário: {nome_usuario} não existe.\nTente novamente com outro usuário ou cadastre-se.', button=QMessageBox.Ok, icon=QMessageBox.Critical)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not  None:
                conn.close()    
class CrudColab():
    @staticmethod
    def Criar_colab(nome,nome_usuario,senha):
        conn = None
        cursor = None
        try:
            conn = Conectar()
            
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute(
                'INSERT INTO public."Colab"(nome, nome_usuario,senha) VALUES (%s, %s, %s)', 
                (nome, nome_usuario, senha )
                )
                conn.commit()
                boxMessage(title=f'Sucesso {nome}',message=f'Seu nome de usuario foi cadastrado:\n\nUsuario : {nome_usuario}',button=QMessageBox.Ok,icon=QMessageBox.Information)
            elif psycopg2.IntegrityError:
                boxMessage(title='Cadastro negado',message=f'O Usuario: {nome_usuario} já existe:\nTente novamente com outro nome',button=QMessageBox.Ok,icon=QMessageBox.Critical)
                return                
        except Exception as e :
            boxMessage(title='Cadastro negado',message=f'Erro ao enviar os dados\n\nProblemas com o banco de dados\nErro : {e}',button=QMessageBox.Ok,icon=QMessageBox.Critical)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not  None:
                conn.close()   
    @staticmethod
    def Ler_colab():
        conn = Conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM public."Colab" ORDER BY id_colab ASC')
        colab = cursor.fetchall()
        cursor.close()
        conn.close()
        return colab
    @staticmethod
    def Atualizar_colab(colab_data):
        try:
            conn = Conectar()
            cursor = conn.cursor()
        
            cursor.execute(
                'UPDATE public."Colab" SET nome = %s, nome_usuario = %s, senha = %s WHERE id_colab = %s',
                (colab_data[1], colab_data[2], colab_data[3], colab_data[0]) 
            )
            conn.commit()

        except Exception as e:
            boxMessage(
                title='Erro',
                message=f'Erro ao atualizar os dados\nErro: {e}',
                button=QMessageBox.Ok,
                icon=QMessageBox.Critical
            )
        finally:
            cursor.close()
            conn.close()


    @staticmethod
    def Deletar_colab(id_colab):
        try:
            conn = Conectar()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM public."Colab" WHERE id_colab = %s', (id_colab,))

            conn.commit()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
class CrudLeitor:
    @staticmethod
    def Criar_leitor(nome,telefone,email,cpf,identidade,cep,escolaridade,data_nascimento,endereco,data_cadastro):
        conn = None
        cursor = None
        
        try:
            conn = Conectar()
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO public."Leitor"(nome,telefone,email,cpf,identidade,cep,escolaridade,data_nascimento,endereco,data_cadastro) VALUES (%s,%s, %s,%s, %s, %s, %s, %s, %s,%s)', 
                    (nome,telefone,email,cpf,identidade,cep,escolaridade,data_nascimento,endereco,data_cadastro)
                )

                conn.commit()
                boxMessage(title=f'Sucesso',message=f'Leitor foi cadastrado:\n\nNome do Leitor : {nome}\n\nCPF do Leitor: {cpf}\n\nIdentidade do Leitor: {identidade}',button=QMessageBox.Ok,icon=QMessageBox.Information)
        except psycopg2.IntegrityError:
                boxMessage(title='Cadastro negado',message=f'O CPF: {cpf} já existe:\nTente novamente com outro CPF',button=QMessageBox.Ok,icon=QMessageBox.Critical)
                return                
        except Exception as e :
                boxMessage(title='Cadastro negado',message=f'Erro ao enviar os dados\n\nProblemas com o banco de dados\nErro : {e}',button=QMessageBox.Ok,icon=QMessageBox.Critical)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not  None:
                conn.close()   

    @staticmethod
    def Ler_leitor():
        conn = Conectar()
        cursor = conn.cursor()
        cursor.execute(
                    'SELECT * FROM public."Leitor" ORDER BY id_leitor'
                )
        leitor = cursor.fetchall()
        cursor.close()
        conn.close()
        return leitor
    @staticmethod
    def Atualizar_leitor(reader_data):
        try:
            conn = Conectar()
            cursor = conn.cursor()
            cursor.execute(
            'UPDATE public."Leitor" SET nome = %s ,telefone = %s,email = %s,cpf = %s,identidade = %s,cep = %s,escolaridade = %s,data_nascimento = %s,endereco = %s,data_cadastro = %s WHERE id_leitor = %s',
            (reader_data[1], reader_data[2],reader_data[3],reader_data[4],reader_data[5],reader_data[6], reader_data[7],reader_data[8],reader_data[9],reader_data[10], reader_data[0]) 
            )
            conn.commit()

        except Exception as e:
            boxMessage(
                title='Erro',
                message=f'Erro ao atualizar os dados\nErro: {e}',
                button=QMessageBox.Ok,
                icon=QMessageBox.Critical
            )
            print(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def Deletar_leitor(id_leitor):
        try:
            conn = Conectar()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM public."Leitor" WHERE id_leitor = %s',(id_leitor,) )
    
            conn.commit()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not  None:
                conn.close()  
class CrudLivros:
    @staticmethod
    def Criar_livro(n_tombo,isbn,editora,ano_edicao,classificacao,n_folhas,titulo_livro,autor,volume,data_cadastro,assunto):
        try:        
            conn = Conectar()
            if conn is not None:   
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO public."Livros"(n_tombo,isbn,editora,ano_edicao,classificacao,n_folhas,titulo_livro,autor,volume,data_cadastro,assunto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', 
                    (n_tombo,isbn,editora,ano_edicao,classificacao,n_folhas,titulo_livro,autor,volume,data_cadastro,assunto)
                )
                conn.commit()
                
                boxMessage(title=f'Sucesso',message=f'Livro foi cadastrado:\n\nTitulo do Livro : {titulo_livro}\n\nNº do TOMBO : {n_tombo}\n\nisbn : {isbn}',button=QMessageBox.Ok,icon=QMessageBox.Information)
        except psycopg2.IntegrityError:
                boxMessage(title='Cadastro negado',message=f'O livro : {titulo_livro}\n\nNº TOMBO {n_tombo}\n\nisbn : {isbn}\n\Já existe, tente novamente com outro numero',button=QMessageBox.Ok,icon=QMessageBox.Critical)
                return                
        except Exception as e :
            boxMessage(title='Cadastro negado',message=f'Erro ao enviar os dados\n\nProblemas com o banco de dados\nErro : {e}',button=QMessageBox.Ok,icon=QMessageBox.Critical)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
    @staticmethod
    def Ler_livro():
        conn = Conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM public."Livros" ORDER BY id_Livro ASC')
        livro = cursor.fetchall()
        cursor.close()
        conn.close()
        return livro
    @staticmethod
    def Atualizar_livro(book_data):
        try:
            conn = Conectar()
            cursor = conn.cursor()
            cursor.execute(
            'UPDATE public."Livros" SET n_tombo = %s,isbn = %s,editora = %s,ano_edicao = %s,classificacao = %s,n_folhas = %s,titulo_livro = %s,autor = %s,volume = %s,data_cadastro = %s,assunto = %s WHERE id_livro = %s',
            (book_data[1], book_data[2],book_data[3],book_data[4],book_data[5],book_data[6], book_data[7],book_data[8],book_data[9],book_data[10],book_data[11], book_data[0]))
            conn.commit()

        except Exception as e:
            boxMessage(
                title='Erro',
                message=f'Erro ao atualizar os dados\nErro: {e}',
                button=QMessageBox.Ok,
                icon=QMessageBox.Critical
            )
        finally:
            cursor.close()
            conn.close()
    @staticmethod
    def Deletar_livro(id_livro):
        try:
            conn = Conectar()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM public."Livros" WHERE id_livro = %s',(id_livro,))
    
            conn.commit()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not  None:
                conn.close()  