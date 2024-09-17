# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ConectUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        MainWindow.setMinimumSize(QtCore.QSize(700, 400))
        MainWindow.setMaximumSize(QtCore.QSize(700, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.container_main = QtWidgets.QWidget(self.centralwidget)
        self.container_main.setStyleSheet("background-color: #5CE1E6;")
        self.container_main.setInputMethodHints(QtCore.Qt.ImhNone)
        self.container_main.setObjectName("container_main")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.container_main)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.container_1 = QtWidgets.QWidget(self.container_main)
        self.container_1.setMaximumSize(QtCore.QSize(350, 400))
        self.container_1.setStyleSheet("")
        self.container_1.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.container_1.setObjectName("container_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.container_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(89, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_1 = QtWidgets.QLabel(self.container_1)
        self.label_1.setMaximumSize(QtCore.QSize(150, 30))
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_4.addWidget(self.label_1)
        spacerItem1 = QtWidgets.QSpacerItem(89, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.frame = QtWidgets.QFrame(self.container_1)
        self.frame.setStyleSheet("QLineEdit{\n"
"background-color: rgb(232, 230, 230);\n"
"max-height:40px;\n"
"border-radius:10px;\n"
"padding:10px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(-1, -1, -1, 40)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(40, 40))
        self.label_3.setMaximumSize(QtCore.QSize(40, 40))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/icons/use.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.inputUser = QtWidgets.QLineEdit(self.frame)
        self.inputUser.setMinimumSize(QtCore.QSize(180, 0))
        self.inputUser.setMaximumSize(QtCore.QSize(180, 60))
        self.inputUser.setStyleSheet("background-color: rgb(232, 230, 230);")
        self.inputUser.setText("")
        self.inputUser.setObjectName("inputUser")
        self.gridLayout.addWidget(self.inputUser, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(50, 20))
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(60, 20))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(40, 40))
        self.label_5.setMaximumSize(QtCore.QSize(40, 40))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icons/icons/cad.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.inputPass = QtWidgets.QLineEdit(self.frame)
        self.inputPass.setMinimumSize(QtCore.QSize(180, 0))
        self.inputPass.setMaximumSize(QtCore.QSize(180, 60))
        self.inputPass.setTabletTracking(False)
        self.inputPass.setStyleSheet("background-color: rgb(232, 230, 230);")
        self.inputPass.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhExclusiveInputMask|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData|QtCore.Qt.ImhUppercaseOnly|QtCore.Qt.ImhUrlCharactersOnly)
        self.inputPass.setInputMask("")
        self.inputPass.setText("")
        self.inputPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPass.setObjectName("inputPass")
        self.gridLayout.addWidget(self.inputPass, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pass_replace = QtWidgets.QPushButton(self.container_1)
        self.pass_replace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pass_replace.setStyleSheet("border: none; color: blue; text-decoration: underline;")
        self.pass_replace.setObjectName("pass_replace")
        self.horizontalLayout_3.addWidget(self.pass_replace)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.frame_2 = QtWidgets.QFrame(self.container_1)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setStyleSheet("QPushButton{\n"
"    background-color: #5CE1E6;    \n"
"    color:#242424;\n"
"    text-align:center;\n"
"    height:30px;\n"
"    border-radius:10px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setHorizontalSpacing(9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonEnt = QtWidgets.QPushButton(self.frame_2)
        self.buttonEnt.setMinimumSize(QtCore.QSize(120, 40))
        self.buttonEnt.setMaximumSize(QtCore.QSize(120, 40))
        self.buttonEnt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonEnt.setAutoFillBackground(False)
        self.buttonEnt.setStyleSheet("background-color: #242424;\n"
"color: rgb(255, 255, 255);")
        self.buttonEnt.setIconSize(QtCore.QSize(16, 16))
        self.buttonEnt.setObjectName("buttonEnt")
        self.gridLayout_3.addWidget(self.buttonEnt, 0, 0, 1, 1)
        self.buttonCad = QtWidgets.QPushButton(self.frame_2)
        self.buttonCad.setMinimumSize(QtCore.QSize(80, 30))
        self.buttonCad.setMaximumSize(QtCore.QSize(80, 30))
        self.buttonCad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonCad.setStyleSheet("background-color:white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/adicionar-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCad.setIcon(icon)
        self.buttonCad.setObjectName("buttonCad")
        self.gridLayout_3.addWidget(self.buttonCad, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_2.addWidget(self.container_1)
        self.container_2 = QtWidgets.QWidget(self.container_main)
        self.container_2.setStyleSheet("background-color: #242424;")
        self.container_2.setObjectName("container_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.container_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_logo = QtWidgets.QLabel(self.container_2)
        self.label_logo.setMaximumSize(QtCore.QSize(250, 250))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/icons/logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setWordWrap(False)
        self.label_logo.setObjectName("label_logo")
        self.gridLayout_2.addWidget(self.label_logo, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.container_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_ver = QtWidgets.QLabel(self.container_2)
        self.label_ver.setObjectName("label_ver")
        self.gridLayout_2.addWidget(self.label_ver, 2, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.container_2)
        self.horizontalLayout.addWidget(self.container_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionCadastrar = QtWidgets.QAction(MainWindow)
        self.actionCadastrar.setObjectName("actionCadastrar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#222222;\">CONECTE-SE</span></p></body></html>"))
        self.inputUser.setPlaceholderText(_translate("MainWindow", "Digite o usuario..."))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#000000;\">Senha:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#000000;\">Usuario:</span></p></body></html>"))
        self.inputPass.setPlaceholderText(_translate("MainWindow", "Digite sua senha..."))
        self.pass_replace.setText(_translate("MainWindow", "Esqueceu a senha?"))
        self.buttonEnt.setWhatsThis(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.buttonEnt.setText(_translate("MainWindow", "Entrar"))
        self.buttonCad.setText(_translate("MainWindow", "Cadastrar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">TECNOLOGIA </span></p><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">DE </span></p><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">ARMAZENAMENTO</span></p></body></html>"))
        self.label_ver.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Versão : 0.01</span></p></body></html>"))
        self.actionCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.actionCadastrar.setToolTip(_translate("MainWindow", "Não tem cadastro? clique-me"))
import imagens_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
