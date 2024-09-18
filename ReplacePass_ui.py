# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReplacePass.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import imagens_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(520, 350)
        Form.setMinimumSize(QSize(520, 350))
        Form.setMaximumSize(QSize(520, 350))
        self.container_5 = QWidget(Form)
        self.container_5.setObjectName(u"container_5")
        self.container_5.setGeometry(QRect(0, 0, 520, 360))
        self.container_5.setMinimumSize(QSize(520, 360))
        self.container_5.setMaximumSize(QSize(520, 350))
        self.container_5.setStyleSheet(u"background-color: #242424;")
        self.horizontalLayout = QHBoxLayout(self.container_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.container_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icons/icons/cad.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 30))
        self.label_19.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.label_19)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(230, 260))
        self.frame.setMaximumSize(QSize(230, 260))
        self.frame.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(232, 230, 230);\n"
"padding-left:10px;\n"
"height:40px;\n"
"border-radius:10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(25, 0))
        self.label_14.setMaximumSize(QSize(30, 30))
        self.label_14.setPixmap(QPixmap(u":/icons/icons/use.png"))
        self.label_14.setScaledContents(True)

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(50, 20))
        self.label_13.setMaximumSize(QSize(100, 20))

        self.gridLayout.addWidget(self.label_13, 2, 1, 1, 1)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(25, 0))
        self.label_16.setMaximumSize(QSize(30, 30))
        self.label_16.setPixmap(QPixmap(u":/icons/icons/chave.png"))
        self.label_16.setScaledContents(True)

        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(50, 20))
        self.label_17.setMaximumSize(QSize(120, 20))

        self.gridLayout.addWidget(self.label_17, 4, 1, 1, 1)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(25, 0))
        self.label_18.setMaximumSize(QSize(30, 30))
        self.label_18.setPixmap(QPixmap(u":/icons/icons/chave.png"))
        self.label_18.setScaledContents(True)

        self.gridLayout.addWidget(self.label_18, 5, 0, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(60, 20))
        self.label_15.setMaximumSize(QSize(60, 20))

        self.gridLayout.addWidget(self.label_15, 0, 1, 1, 1)

        self.inputUser_3 = QLineEdit(self.frame)
        self.inputUser_3.setObjectName(u"inputUser_3")
        self.inputUser_3.setMinimumSize(QSize(0, 0))
        self.inputUser_3.setMaximumSize(QSize(16777215, 16777215))
        self.inputUser_3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.inputUser_3, 1, 1, 1, 1)

        self.inputPass_3 = QLineEdit(self.frame)
        self.inputPass_3.setObjectName(u"inputPass_3")
        self.inputPass_3.setMinimumSize(QSize(0, 0))
        self.inputPass_3.setMaximumSize(QSize(16777215, 16777215))
        self.inputPass_3.setTabletTracking(False)
        self.inputPass_3.setStyleSheet(u"")
        self.inputPass_3.setInputMethodHints(Qt.ImhDate|Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhEmailCharactersOnly|Qt.ImhExclusiveInputMask|Qt.ImhFormattedNumbersOnly|Qt.ImhHiddenText|Qt.ImhLatinOnly|Qt.ImhLowercaseOnly|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData|Qt.ImhUppercaseOnly|Qt.ImhUrlCharactersOnly)
        self.inputPass_3.setInputMask(u"")
        self.inputPass_3.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.inputPass_3, 3, 1, 1, 1)

        self.inputPass_4 = QLineEdit(self.frame)
        self.inputPass_4.setObjectName(u"inputPass_4")
        self.inputPass_4.setMinimumSize(QSize(0, 0))
        self.inputPass_4.setMaximumSize(QSize(16777215, 16777215))
        self.inputPass_4.setTabletTracking(False)
        self.inputPass_4.setStyleSheet(u"")
        self.inputPass_4.setInputMethodHints(Qt.ImhDate|Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhEmailCharactersOnly|Qt.ImhExclusiveInputMask|Qt.ImhFormattedNumbersOnly|Qt.ImhHiddenText|Qt.ImhLatinOnly|Qt.ImhLowercaseOnly|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData|Qt.ImhUppercaseOnly|Qt.ImhUrlCharactersOnly)
        self.inputPass_4.setInputMask(u"")
        self.inputPass_4.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.inputPass_4, 5, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.container_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(240, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_logo_4 = QLabel(self.frame_5)
        self.label_logo_4.setObjectName(u"label_logo_4")
        self.label_logo_4.setMinimumSize(QSize(120, 120))
        self.label_logo_4.setMaximumSize(QSize(120, 120))
        self.label_logo_4.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_logo_4.setScaledContents(True)
        self.label_logo_4.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_logo_4, 0, 1, 1, 1)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(220, 50))

        self.gridLayout_2.addWidget(self.label_20, 1, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"color:black;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.button_return = QPushButton(self.frame_4)
        self.button_return.setObjectName(u"button_return")
        self.button_return.setGeometry(QRect(80, 72, 80, 30))
        self.button_return.setMinimumSize(QSize(80, 30))
        self.button_return.setMaximumSize(QSize(80, 30))
        self.button_return.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_return.setStyleSheet(u"background-color: white;\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/angulo-quadrado-esquerdo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_return.setIcon(icon)
        self.button_save = QPushButton(self.frame_4)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(60, 18, 120, 40))
        self.button_save.setMinimumSize(QSize(120, 40))
        self.button_save.setMaximumSize(QSize(120, 40))
        self.button_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_save.setAutoFillBackground(False)
        self.button_save.setStyleSheet(u"background-color: #5CE1E6;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/angulo-quadrado-direito.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_save.setIcon(icon1)
        self.button_save.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_19.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#cae8ff;\">Mudar senha</span></p></body></html>", None))
        self.label_14.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; color:#cae8ff;\">Nova Senha:</span></p></body></html>", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; color:#cae8ff;\">Repita a senha:</span></p></body></html>", None))
        self.label_18.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; color:#cae8ff;\">Usuario:</span></p></body></html>", None))
        self.inputUser_3.setText("")
        self.inputUser_3.setPlaceholderText(QCoreApplication.translate("Form", u"Digite o usuario...", None))
        self.inputPass_3.setText("")
        self.inputPass_3.setPlaceholderText(QCoreApplication.translate("Form", u"Digite sua senha...", None))
        self.inputPass_4.setText("")
        self.inputPass_4.setPlaceholderText(QCoreApplication.translate("Form", u"Digite sua senha...", None))
        self.label_logo_4.setText("")
        self.label_20.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; color:#cae8ff;\">-&gt; Caso esque\u00e7a do usu\u00e1rio </span></p><p><span style=\" font-size:10pt; color:#cae8ff;\">ter\u00e1 que ser feito um novo cadastro!</span></p></body></html>", None))
        self.button_return.setText(QCoreApplication.translate("Form", u"Voltar", None))
#if QT_CONFIG(whatsthis)
        self.button_save.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p/></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.button_save.setText(QCoreApplication.translate("Form", u"Salvar", None))
    # retranslateUi

