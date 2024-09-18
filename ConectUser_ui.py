# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConectUser.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import imagens_rc
import imagens_rc
import imagens_rc
import imagens_rc
import imagens_rc
import imagens_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 400)
        MainWindow.setMinimumSize(QSize(700, 400))
        MainWindow.setMaximumSize(QSize(700, 400))
        self.actionCadastrar = QAction(MainWindow)
        self.actionCadastrar.setObjectName(u"actionCadastrar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.container_main = QWidget(self.centralwidget)
        self.container_main.setObjectName(u"container_main")
        self.container_main.setStyleSheet(u"background-color: #5CE1E6;")
        self.container_main.setInputMethodHints(Qt.ImhNone)
        self.horizontalLayout_2 = QHBoxLayout(self.container_main)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.container_1 = QWidget(self.container_main)
        self.container_1.setObjectName(u"container_1")
        self.container_1.setMaximumSize(QSize(350, 400))
        self.container_1.setStyleSheet(u"")
        self.container_1.setInputMethodHints(Qt.ImhPreferNumbers)
        self.verticalLayout = QVBoxLayout(self.container_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(89, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_1 = QLabel(self.container_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_4.addWidget(self.label_1)

        self.horizontalSpacer = QSpacerItem(89, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.frame = QFrame(self.container_1)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(232, 230, 230);\n"
"max-height:40px;\n"
"border-radius:10px;\n"
"padding:10px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 40)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(40, 40))
        self.label_3.setMaximumSize(QSize(40, 40))
        self.label_3.setPixmap(QPixmap(u":/icons/icons/use.png"))
        self.label_3.setScaledContents(True)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.inputUser = QLineEdit(self.frame)
        self.inputUser.setObjectName(u"inputUser")
        self.inputUser.setMinimumSize(QSize(180, 0))
        self.inputUser.setMaximumSize(QSize(180, 60))
        self.inputUser.setStyleSheet(u"background-color: rgb(232, 230, 230);")

        self.gridLayout.addWidget(self.inputUser, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 20))
        self.label_4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 20))
        self.label_2.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/icons/icons/cad.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.inputPass = QLineEdit(self.frame)
        self.inputPass.setObjectName(u"inputPass")
        self.inputPass.setMinimumSize(QSize(180, 0))
        self.inputPass.setMaximumSize(QSize(180, 60))
        self.inputPass.setTabletTracking(False)
        self.inputPass.setStyleSheet(u"background-color: rgb(232, 230, 230);")
        self.inputPass.setInputMethodHints(Qt.ImhDate|Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhEmailCharactersOnly|Qt.ImhExclusiveInputMask|Qt.ImhFormattedNumbersOnly|Qt.ImhHiddenText|Qt.ImhLatinOnly|Qt.ImhLowercaseOnly|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData|Qt.ImhUppercaseOnly|Qt.ImhUrlCharactersOnly)
        self.inputPass.setInputMask(u"")
        self.inputPass.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.inputPass, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pass_replace = QPushButton(self.container_1)
        self.pass_replace.setObjectName(u"pass_replace")
        self.pass_replace.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pass_replace.setStyleSheet(u"border: none; color: blue; text-decoration: underline;")

        self.horizontalLayout_3.addWidget(self.pass_replace)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.frame_2 = QFrame(self.container_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #5CE1E6;	\n"
"	color:#242424;\n"
"	text-align:center;\n"
"	height:30px;\n"
"	border-radius:10px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(9)
        self.buttonEnt = QPushButton(self.frame_2)
        self.buttonEnt.setObjectName(u"buttonEnt")
        self.buttonEnt.setMinimumSize(QSize(120, 40))
        self.buttonEnt.setMaximumSize(QSize(120, 40))
        self.buttonEnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonEnt.setAutoFillBackground(False)
        self.buttonEnt.setStyleSheet(u"background-color: #242424;\n"
"color: rgb(255, 255, 255);")
        self.buttonEnt.setIconSize(QSize(16, 16))

        self.gridLayout_3.addWidget(self.buttonEnt, 0, 0, 1, 1)

        self.buttonCad = QPushButton(self.frame_2)
        self.buttonCad.setObjectName(u"buttonCad")
        self.buttonCad.setMinimumSize(QSize(80, 30))
        self.buttonCad.setMaximumSize(QSize(80, 30))
        self.buttonCad.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonCad.setStyleSheet(u"background-color:white;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/adicionar-usuario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonCad.setIcon(icon)

        self.gridLayout_3.addWidget(self.buttonCad, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.container_1)

        self.container_2 = QWidget(self.container_main)
        self.container_2.setObjectName(u"container_2")
        self.container_2.setStyleSheet(u"background-color: #242424;")
        self.gridLayout_2 = QGridLayout(self.container_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_logo = QLabel(self.container_2)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMaximumSize(QSize(250, 250))
        self.label_logo.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_logo, 0, 0, 1, 1)

        self.label = QLabel(self.container_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_ver = QLabel(self.container_2)
        self.label_ver.setObjectName(u"label_ver")

        self.gridLayout_2.addWidget(self.label_ver, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.container_2)


        self.horizontalLayout.addWidget(self.container_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
#if QT_CONFIG(tooltip)
        self.actionCadastrar.setToolTip(QCoreApplication.translate("MainWindow", u"N\u00e3o tem cadastro? clique-me", None))
#endif // QT_CONFIG(tooltip)
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#222222;\">CONECTE-SE</span></p></body></html>", None))
        self.label_3.setText("")
        self.inputUser.setText("")
        self.inputUser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o usuario...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#000000;\">Senha:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#000000;\">Usuario:</span></p></body></html>", None))
        self.label_5.setText("")
        self.inputPass.setText("")
        self.inputPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha...", None))
        self.pass_replace.setText(QCoreApplication.translate("MainWindow", u"Esqueceu a senha?", None))
#if QT_CONFIG(whatsthis)
        self.buttonEnt.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.buttonEnt.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.buttonCad.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">TECNOLOGIA </span></p><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">DE </span></p><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">ARMAZENAMENTO</span></p></body></html>", None))
        self.label_ver.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Vers\u00e3o : 0.01</span></p></body></html>", None))
    # retranslateUi

