# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterUser.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import imagens_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 500)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(850, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(850, 850))
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.container_main = QFrame(self.centralwidget)
        self.container_main.setObjectName(u"container_main")
        self.container_main.setMinimumSize(QSize(850, 500))
        self.container_main.setMaximumSize(QSize(850, 500))
        self.container_main.setStyleSheet(u"background-color: #242424;")
        self.container_main.setInputMethodHints(Qt.ImhNone)
        self.gridLayout_6 = QGridLayout(self.container_main)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.container_1 = QFrame(self.container_main)
        self.container_1.setObjectName(u"container_1")
        self.container_1.setMaximumSize(QSize(16777215, 16777215))
        self.container_1.setStyleSheet(u"")
        self.container_1.setInputMethodHints(Qt.ImhPreferNumbers)
        self.gridLayout_4 = QGridLayout(self.container_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(self.container_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icons/icons/cedula.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_a = QLabel(self.frame)
        self.label_a.setObjectName(u"label_a")
        self.label_a.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.label_a)

        self.label_b = QLabel(self.frame)
        self.label_b.setObjectName(u"label_b")

        self.verticalLayout.addWidget(self.label_b)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.container_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(232, 230, 230);\n"
"max-height:40px;\n"
"border-radius:10px;\n"
"padding:10px;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.label_c = QLabel(self.frame_2)
        self.label_c.setObjectName(u"label_c")
        self.label_c.setMinimumSize(QSize(60, 20))
        self.label_c.setMaximumSize(QSize(200, 20))

        self.gridLayout.addWidget(self.label_c, 0, 1, 1, 2)

        self.input_novousuario = QLineEdit(self.frame_2)
        self.input_novousuario.setObjectName(u"input_novousuario")
        self.input_novousuario.setMinimumSize(QSize(180, 30))
        self.input_novousuario.setMaximumSize(QSize(180, 60))
        self.input_novousuario.setStyleSheet(u"background-color: rgb(232, 230, 230);")

        self.gridLayout.addWidget(self.input_novousuario, 1, 4, 1, 2)

        self.label_d = QLabel(self.frame_2)
        self.label_d.setObjectName(u"label_d")
        self.label_d.setMinimumSize(QSize(60, 20))
        self.label_d.setMaximumSize(QSize(200, 20))

        self.gridLayout.addWidget(self.label_d, 0, 4, 1, 1)

        self.label_i = QLabel(self.frame_2)
        self.label_i.setObjectName(u"label_i")
        self.label_i.setMinimumSize(QSize(30, 30))
        self.label_i.setMaximumSize(QSize(30, 30))
        self.label_i.setPixmap(QPixmap(u":/icons/icons/chave.png"))
        self.label_i.setScaledContents(True)

        self.gridLayout.addWidget(self.label_i, 3, 0, 1, 1)

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background-color:transparent;")

        self.gridLayout.addWidget(self.label_21, 0, 5, 1, 1)

        self.label_e = QLabel(self.frame_2)
        self.label_e.setObjectName(u"label_e")
        self.label_e.setMinimumSize(QSize(50, 20))
        self.label_e.setMaximumSize(QSize(130, 20))

        self.gridLayout.addWidget(self.label_e, 2, 1, 1, 1)

        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"background-color:transparent;")

        self.gridLayout.addWidget(self.label_22, 2, 2, 1, 1)

        self.label_f = QLabel(self.frame_2)
        self.label_f.setObjectName(u"label_f")
        self.label_f.setMinimumSize(QSize(125, 20))
        self.label_f.setMaximumSize(QSize(125, 20))

        self.gridLayout.addWidget(self.label_f, 2, 4, 1, 2)

        self.input_nome = QLineEdit(self.frame_2)
        self.input_nome.setObjectName(u"input_nome")
        self.input_nome.setMinimumSize(QSize(180, 30))
        self.input_nome.setMaximumSize(QSize(180, 60))
        self.input_nome.setStyleSheet(u"background-color: rgb(232, 230, 230);")

        self.gridLayout.addWidget(self.input_nome, 1, 1, 1, 2)

        self.input_novasenha = QLineEdit(self.frame_2)
        self.input_novasenha.setObjectName(u"input_novasenha")
        self.input_novasenha.setMinimumSize(QSize(180, 30))
        self.input_novasenha.setMaximumSize(QSize(180, 60))
        self.input_novasenha.setTabletTracking(False)
        self.input_novasenha.setStyleSheet(u"background-color: rgb(232, 230, 230);")
        self.input_novasenha.setInputMethodHints(Qt.ImhDate|Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhEmailCharactersOnly|Qt.ImhExclusiveInputMask|Qt.ImhFormattedNumbersOnly|Qt.ImhHiddenText|Qt.ImhLatinOnly|Qt.ImhLowercaseOnly|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData|Qt.ImhUppercaseOnly|Qt.ImhUrlCharactersOnly)
        self.input_novasenha.setInputMask(u"")
        self.input_novasenha.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.input_novasenha, 3, 1, 1, 2)

        self.input_confirmasenha = QLineEdit(self.frame_2)
        self.input_confirmasenha.setObjectName(u"input_confirmasenha")
        self.input_confirmasenha.setMinimumSize(QSize(180, 30))
        self.input_confirmasenha.setMaximumSize(QSize(180, 60))
        self.input_confirmasenha.setTabletTracking(False)
        self.input_confirmasenha.setStyleSheet(u"background-color: rgb(232, 230, 230);")
        self.input_confirmasenha.setInputMethodHints(Qt.ImhDate|Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhEmailCharactersOnly|Qt.ImhExclusiveInputMask|Qt.ImhFormattedNumbersOnly|Qt.ImhHiddenText|Qt.ImhLatinOnly|Qt.ImhLowercaseOnly|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData|Qt.ImhUppercaseOnly|Qt.ImhUrlCharactersOnly)
        self.input_confirmasenha.setInputMask(u"")
        self.input_confirmasenha.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.input_confirmasenha, 3, 4, 1, 2)

        self.label_j = QLabel(self.frame_2)
        self.label_j.setObjectName(u"label_j")
        self.label_j.setMinimumSize(QSize(30, 30))
        self.label_j.setMaximumSize(QSize(30, 30))
        self.label_j.setPixmap(QPixmap(u":/icons/icons/chave.png"))
        self.label_j.setScaledContents(True)

        self.gridLayout.addWidget(self.label_j, 3, 3, 1, 1)

        self.label_h = QLabel(self.frame_2)
        self.label_h.setObjectName(u"label_h")
        self.label_h.setMinimumSize(QSize(30, 30))
        self.label_h.setMaximumSize(QSize(30, 30))
        self.label_h.setStyleSheet(u"")
        self.label_h.setPixmap(QPixmap(u":/icons/icons/use.png"))
        self.label_h.setScaledContents(True)

        self.gridLayout.addWidget(self.label_h, 1, 3, 1, 1)

        self.label_g = QLabel(self.frame_2)
        self.label_g.setObjectName(u"label_g")
        self.label_g.setMinimumSize(QSize(30, 30))
        self.label_g.setMaximumSize(QSize(30, 30))
        self.label_g.setStyleSheet(u"")
        self.label_g.setPixmap(QPixmap(u":/icons/icons/use.png"))
        self.label_g.setScaledContents(True)

        self.gridLayout.addWidget(self.label_g, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)

        self.label_20 = QLabel(self.container_1)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_k = QLabel(self.container_1)
        self.label_k.setObjectName(u"label_k")
        self.label_k.setMaximumSize(QSize(340, 100))

        self.horizontalLayout_2.addWidget(self.label_k)

        self.pushButton_LGPD = QPushButton(self.container_1)
        self.pushButton_LGPD.setObjectName(u"pushButton_LGPD")
        self.pushButton_LGPD.setMinimumSize(QSize(50, 0))
        self.pushButton_LGPD.setMaximumSize(QSize(50, 16777215))
        self.pushButton_LGPD.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_LGPD.setStyleSheet(u"border: none; color:#5CE1E6; text-decoration: underline;")

        self.horizontalLayout_2.addWidget(self.pushButton_LGPD)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.frame_3 = QFrame(self.container_1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"color:black;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_registrar = QPushButton(self.frame_3)
        self.button_registrar.setObjectName(u"button_registrar")
        self.button_registrar.setMinimumSize(QSize(120, 40))
        self.button_registrar.setMaximumSize(QSize(120, 40))
        self.button_registrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_registrar.setAutoFillBackground(False)
        self.button_registrar.setStyleSheet(u"background-color: green;	\n"
"color: white;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/adicionar-usuario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_registrar.setIcon(icon)
        self.button_registrar.setIconSize(QSize(16, 16))

        self.gridLayout_2.addWidget(self.button_registrar, 0, 0, 1, 1)

        self.button_voltar = QPushButton(self.frame_3)
        self.button_voltar.setObjectName(u"button_voltar")
        self.button_voltar.setMinimumSize(QSize(80, 30))
        self.button_voltar.setMaximumSize(QSize(80, 30))
        self.button_voltar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_voltar.setStyleSheet(u"background-color: #5CE1E6;\n"
"color: #242424 ;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/angulo-quadrado-esquerdo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_voltar.setIcon(icon1)

        self.gridLayout_2.addWidget(self.button_voltar, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 4, 0, 1, 1)


        self.gridLayout_6.addWidget(self.container_1, 0, 0, 1, 1)

        self.container_2 = QFrame(self.container_main)
        self.container_2.setObjectName(u"container_2")
        self.container_2.setMaximumSize(QSize(350, 16777215))
        self.container_2.setStyleSheet(u"background-color: #cae8ff;\n"
"")
        self.gridLayout_5 = QGridLayout(self.container_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_tit_regi = QLabel(self.container_2)
        self.label_tit_regi.setObjectName(u"label_tit_regi")

        self.gridLayout_5.addWidget(self.label_tit_regi, 1, 0, 1, 1)

        self.label_ver_regi = QLabel(self.container_2)
        self.label_ver_regi.setObjectName(u"label_ver_regi")
        self.label_ver_regi.setMaximumSize(QSize(16777215, 20))
        self.label_ver_regi.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_ver_regi, 2, 0, 1, 1)

        self.label_logoreg = QLabel(self.container_2)
        self.label_logoreg.setObjectName(u"label_logoreg")
        self.label_logoreg.setMinimumSize(QSize(250, 250))
        self.label_logoreg.setMaximumSize(QSize(250, 250))
        self.label_logoreg.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_logoreg.setScaledContents(True)
        self.label_logoreg.setWordWrap(False)

        self.gridLayout_5.addWidget(self.label_logoreg, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.container_2, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.container_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.input_nome, self.input_novousuario)
        QWidget.setTabOrder(self.input_novousuario, self.input_novasenha)
        QWidget.setTabOrder(self.input_novasenha, self.input_confirmasenha)
        QWidget.setTabOrder(self.input_confirmasenha, self.pushButton_LGPD)
        QWidget.setTabOrder(self.pushButton_LGPD, self.button_registrar)
        QWidget.setTabOrder(self.button_registrar, self.button_voltar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_a.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#cae8ff;\">CADASTRE-SE</span></p></body></html>", None))
        self.label_b.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#cae8ff;\">Complete o formulario abaixo para realizar seu cadastro na LIBRYNO.</span></p></body></html>", None))
        self.label_c.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#cae8ff;\">Seu nome:</span></p></body></html>", None))
        self.input_novousuario.setText("")
        self.input_novousuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome de usuario...", None))
        self.label_d.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#cae8ff;\">Usu\u00e1rio:*</span></p></body></html>", None))
        self.label_i.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#5ce1e6;\">* Campo importante</span></p></body></html>", None))
        self.label_e.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#cae8ff;\">Senha:*</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#5ce1e6;\">* Campo importante</span></p></body></html>", None))
        self.label_f.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#cae8ff;\">Confirmar Senha:</span></p></body></html>", None))
        self.input_nome.setText("")
        self.input_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome...", None))
        self.input_novasenha.setText("")
        self.input_novasenha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite uma senha...", None))
        self.input_confirmasenha.setText("")
        self.input_confirmasenha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirme a senha escolhida...", None))
        self.label_j.setText("")
        self.label_h.setText("")
        self.label_g.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#cae8ff;\">* N\u00e3o esque\u00e7a do seu usu\u00e1rio</span></p><p><span style=\" font-size:10pt; color:#cae8ff;\">* Voc\u00ea consiguir\u00e1 resgatar sua senha futuramente.</span></p></body></html>", None))
        self.label_k.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#cae8ff;\">Seus dados estar\u00e3o seguros, conforme </span><span style=\" color:#5ce1e6;\">Lei n\u00b0 13.709/2018</span><span style=\" font-size:10pt; color:#cae8ff;\"> -&gt; </span></p></body></html>", None))
        self.pushButton_LGPD.setText(QCoreApplication.translate("MainWindow", u"LGPD", None))
#if QT_CONFIG(whatsthis)
        self.button_registrar.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.button_registrar.setText(QCoreApplication.translate("MainWindow", u"Registar", None))
        self.button_voltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_tit_regi.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#242424;\">TECNOLOGIA </span></p><p align=\"center\"><span style=\" font-size:14pt; color:#242424;\">DE </span></p><p align=\"center\"><span style=\" font-size:14pt; color:#242424;\">ARMAZENAMENTO</span></p></body></html>", None))
        self.label_ver_regi.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" color:#242424;\">Vers\u00e3o : 0.01</span></p></body></html>", None))
        self.label_logoreg.setText("")
    # retranslateUi

