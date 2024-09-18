# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeUser - Copia.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import imagens_rc
import imagens_rc
import imagens_rc
import imagens_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 580)
        MainWindow.setMinimumSize(QSize(1000, 580))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color:#cae8ff;\n"
"	color: Black;\n"
"}\n"
"QPushButton{\n"
"	color:Black;\n"
"	text-align:center;\n"
"	height:50px;\n"
"	border: none;\n"
"	border-radius:10px;\n"
"	\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:#5CE1E6;\n"
"}")
        self.gridLayout_11 = QGridLayout(self.widget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButton_Return_Connect2 = QPushButton(self.widget)
        self.pushButton_Return_Connect2.setObjectName(u"pushButton_Return_Connect2")
        self.pushButton_Return_Connect2.setMinimumSize(QSize(30, 30))
        self.pushButton_Return_Connect2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Return_Connect2.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/angulo-circulo-esquerda.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Return_Connect2.setIcon(icon)
        self.pushButton_Return_Connect2.setIconSize(QSize(25, 25))
        self.pushButton_Return_Connect2.setCheckable(False)

        self.gridLayout_11.addWidget(self.pushButton_Return_Connect2, 2, 0, 1, 1)

        self.Nav2 = QFrame(self.widget)
        self.Nav2.setObjectName(u"Nav2")
        self.Nav2.setFrameShape(QFrame.StyledPanel)
        self.Nav2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Nav2)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_home2 = QPushButton(self.Nav2)
        self.pushButton_home2.setObjectName(u"pushButton_home2")
        self.pushButton_home2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/casa.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_home2.setIcon(icon1)
        self.pushButton_home2.setIconSize(QSize(30, 30))
        self.pushButton_home2.setCheckable(True)
        self.pushButton_home2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_home2)

        self.pushButton_lib2 = QPushButton(self.Nav2)
        self.pushButton_lib2.setObjectName(u"pushButton_lib2")
        self.pushButton_lib2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/livros.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_lib2.setIcon(icon2)
        self.pushButton_lib2.setIconSize(QSize(25, 25))
        self.pushButton_lib2.setCheckable(True)
        self.pushButton_lib2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_lib2)

        self.pushButton_reader2 = QPushButton(self.Nav2)
        self.pushButton_reader2.setObjectName(u"pushButton_reader2")
        self.pushButton_reader2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/leitor-de-livro-aberto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_reader2.setIcon(icon3)
        self.pushButton_reader2.setIconSize(QSize(30, 30))
        self.pushButton_reader2.setCheckable(True)
        self.pushButton_reader2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_reader2)

        self.pushButton_colab2 = QPushButton(self.Nav2)
        self.pushButton_colab2.setObjectName(u"pushButton_colab2")
        self.pushButton_colab2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/grupo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_colab2.setIcon(icon4)
        self.pushButton_colab2.setIconSize(QSize(40, 40))
        self.pushButton_colab2.setCheckable(True)
        self.pushButton_colab2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_colab2)

        self.pushButton_on2 = QPushButton(self.Nav2)
        self.pushButton_on2.setObjectName(u"pushButton_on2")
        self.pushButton_on2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/comentario-pergunta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_on2.setIcon(icon5)
        self.pushButton_on2.setIconSize(QSize(30, 30))
        self.pushButton_on2.setCheckable(True)
        self.pushButton_on2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_on2)


        self.gridLayout_11.addWidget(self.Nav2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 294, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        self.gridLayout_12 = QGridLayout(self.widget_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QWidget{	\n"
"	background-color: #cae8ff;\n"
"	color: Black;\n"
"}\n"
"QPushButton{\n"
"	color:Black;\n"
"	height:30px;\n"
"	border: none;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}")
        self.gridLayout_13 = QGridLayout(self.widget_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.pushButton_Menu = QPushButton(self.widget_4)
        self.pushButton_Menu.setObjectName(u"pushButton_Menu")
        self.pushButton_Menu.setMinimumSize(QSize(40, 40))
        self.pushButton_Menu.setMaximumSize(QSize(40, 40))
        self.pushButton_Menu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Menu.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:#5CE1E6;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Menu.setIcon(icon6)
        self.pushButton_Menu.setIconSize(QSize(30, 30))
        self.pushButton_Menu.setCheckable(True)

        self.gridLayout_13.addWidget(self.pushButton_Menu, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(232, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.pushButton_Perfil_Colab = QPushButton(self.widget_4)
        self.pushButton_Perfil_Colab.setObjectName(u"pushButton_Perfil_Colab")
        self.pushButton_Perfil_Colab.setMinimumSize(QSize(40, 40))
        self.pushButton_Perfil_Colab.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Perfil_Colab.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:#5CE1E6;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/perfil-de-usuario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Perfil_Colab.setIcon(icon7)
        self.pushButton_Perfil_Colab.setIconSize(QSize(25, 25))
        self.pushButton_Perfil_Colab.setCheckable(True)
        self.pushButton_Perfil_Colab.setAutoExclusive(True)

        self.gridLayout_13.addWidget(self.pushButton_Perfil_Colab, 0, 4, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_Seach_Home = QLineEdit(self.widget_4)
        self.input_Seach_Home.setObjectName(u"input_Seach_Home")
        self.input_Seach_Home.setMinimumSize(QSize(200, 30))
        self.input_Seach_Home.setStyleSheet(u"padding-left:10px;")

        self.horizontalLayout.addWidget(self.input_Seach_Home)

        self.pushButton_Seach_Home = QPushButton(self.widget_4)
        self.pushButton_Seach_Home.setObjectName(u"pushButton_Seach_Home")
        self.pushButton_Seach_Home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/pesquisar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Seach_Home.setIcon(icon8)
        self.pushButton_Seach_Home.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pushButton_Seach_Home)


        self.gridLayout_13.addLayout(self.horizontalLayout, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(232, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer, 0, 3, 1, 1)


        self.gridLayout_12.addWidget(self.widget_4, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.widget_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_13.addWidget(self.label_5)


        self.gridLayout_12.addWidget(self.frame_4, 2, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.horizontalLayout_2 = QHBoxLayout(self.pageHome)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.pageHome)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.stackedWidget.addWidget(self.pageHome)
        self.page_Lib = QWidget()
        self.page_Lib.setObjectName(u"page_Lib")
        self.verticalLayout_3 = QVBoxLayout(self.page_Lib)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.tabWidget_2 = QTabWidget(self.page_Lib)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setStyleSheet(u"QTabBar::tab {\n"
"                width: 0px;  \n"
"                padding: 0px; \n"
"                margin: 0px; \n"
"            }")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_7 = QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.tab_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QWidget{	\n"
"	background-color: #cae8ff;\n"
"	color: Black;\n"
"}\n"
"QPushButton{\n"
"	background-color: #5CE1E6;	\n"
"	color:#242424;\n"
"	border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/abra-o-livro.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_10.addWidget(self.label_17)

        self.pushButton_Refresh_B = QPushButton(self.frame)
        self.pushButton_Refresh_B.setObjectName(u"pushButton_Refresh_B")
        self.pushButton_Refresh_B.setMinimumSize(QSize(40, 40))
        self.pushButton_Refresh_B.setMaximumSize(QSize(40, 40))
        self.pushButton_Refresh_B.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/sincronizar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Refresh_B.setIcon(icon9)
        self.pushButton_Refresh_B.setIconSize(QSize(25, 25))

        self.horizontalLayout_10.addWidget(self.pushButton_Refresh_B)


        self.verticalLayout_7.addWidget(self.frame)

        self.tableWidget_B = QTableWidget(self.tab_3)
        if (self.tableWidget_B.columnCount() < 12):
            self.tableWidget_B.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableWidget_B.setObjectName(u"tableWidget_B")

        self.verticalLayout_7.addWidget(self.tableWidget_B)

        self.frame_9 = QFrame(self.tab_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QWidget{	\n"
"	background-color: #cae8ff;\n"
"	color: Black;\n"
"}\n"
"QPushButton{\n"
"	background-color: #5CE1E6;	\n"
"	color:#242424;\n"
"	text-align:center;\n"
"	height:30px;\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_Cad_B_Page = QPushButton(self.frame_9)
        self.pushButton_Cad_B_Page.setObjectName(u"pushButton_Cad_B_Page")
        self.pushButton_Cad_B_Page.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Cad_B_Page.setStyleSheet(u"background-color: green;\n"
"color:white;	")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/camada-mais.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Cad_B_Page.setIcon(icon10)
        self.pushButton_Cad_B_Page.setAutoExclusive(False)

        self.horizontalLayout_9.addWidget(self.pushButton_Cad_B_Page)

        self.line_10 = QFrame(self.frame_9)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_10)

        self.pushButton_Update_B = QPushButton(self.frame_9)
        self.pushButton_Update_B.setObjectName(u"pushButton_Update_B")
        self.pushButton_Update_B.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Update_B.setMouseTracking(False)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/documento2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Update_B.setIcon(icon11)

        self.horizontalLayout_9.addWidget(self.pushButton_Update_B)

        self.line_11 = QFrame(self.frame_9)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_11)

        self.pushButton_Delete_B = QPushButton(self.frame_9)
        self.pushButton_Delete_B.setObjectName(u"pushButton_Delete_B")
        self.pushButton_Delete_B.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Delete_B.setStyleSheet(u"background-color: red;\n"
"color:white;	")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/lixeira.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Delete_B.setIcon(icon12)

        self.horizontalLayout_9.addWidget(self.pushButton_Delete_B)

        self.line_12 = QFrame(self.frame_9)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_12)

        self.pushButton_Export_Excel_B = QPushButton(self.frame_9)
        self.pushButton_Export_Excel_B.setObjectName(u"pushButton_Export_Excel_B")
        self.pushButton_Export_Excel_B.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/seta-circulo-para-baixo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Export_Excel_B.setIcon(icon13)

        self.horizontalLayout_9.addWidget(self.pushButton_Export_Excel_B)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_10 = QFrame(self.tab_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(420, 60))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(40, 40))
        self.label_9.setMaximumSize(QSize(40, 40))
        self.label_9.setPixmap(QPixmap(u":/icons/icons/camada-mais.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_9)

        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(420, 30))

        self.horizontalLayout_15.addWidget(self.label_18)


        self.gridLayout_4.addWidget(self.frame_15, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(420, 16777215))
        self.frame_12.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(232, 230, 230);\n"
"height:40px;\n"
"border-radius:10px;\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(232, 230, 230);\n"
"border-radius:10px;\n"
"}\n"
"QLabel{\n"
"qproperty-alignment: 'AlignCenter';\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_D_Cad_B = QLineEdit(self.frame_12)
        self.lineEdit_D_Cad_B.setObjectName(u"lineEdit_D_Cad_B")
        self.lineEdit_D_Cad_B.setMinimumSize(QSize(0, 0))
        self.lineEdit_D_Cad_B.setCursorPosition(0)
        self.lineEdit_D_Cad_B.setAlignment(Qt.AlignCenter)
        self.lineEdit_D_Cad_B.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_D_Cad_B.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.lineEdit_D_Cad_B, 13, 1, 1, 1)

        self.lineEdit_Num_Tombo_B = QLineEdit(self.frame_12)
        self.lineEdit_Num_Tombo_B.setObjectName(u"lineEdit_Num_Tombo_B")
        self.lineEdit_Num_Tombo_B.setMinimumSize(QSize(0, 0))
        self.lineEdit_Num_Tombo_B.setMaxLength(3276700)
        self.lineEdit_Num_Tombo_B.setAlignment(Qt.AlignCenter)
        self.lineEdit_Num_Tombo_B.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_Num_Tombo_B.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_Num_Tombo_B, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)

        self.lineEdit_ISBM_B = QLineEdit(self.frame_12)
        self.lineEdit_ISBM_B.setObjectName(u"lineEdit_ISBM_B")
        self.lineEdit_ISBM_B.setMinimumSize(QSize(0, 0))
        self.lineEdit_ISBM_B.setMaxLength(3276700)
        self.lineEdit_ISBM_B.setAlignment(Qt.AlignCenter)
        self.lineEdit_ISBM_B.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.lineEdit_ISBM_B, 1, 1, 1, 1)

        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 2, 1, 1, 1)

        self.label_22 = QLabel(self.frame_12)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 11, 0, 1, 1)

        self.lineEdit_Title_B = QLineEdit(self.frame_12)
        self.lineEdit_Title_B.setObjectName(u"lineEdit_Title_B")
        self.lineEdit_Title_B.setMinimumSize(QSize(0, 0))
        self.lineEdit_Title_B.setAlignment(Qt.AlignCenter)
        self.lineEdit_Title_B.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.lineEdit_Title_B, 7, 0, 1, 2)

        self.lineEdit_Name_A_B = QLineEdit(self.frame_12)
        self.lineEdit_Name_A_B.setObjectName(u"lineEdit_Name_A_B")
        self.lineEdit_Name_A_B.setAlignment(Qt.AlignCenter)
        self.lineEdit_Name_A_B.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.lineEdit_Name_A_B, 10, 0, 1, 2)

        self.label_23 = QLabel(self.frame_12)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 11, 1, 1, 1)

        self.label_21 = QLabel(self.frame_12)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 9, 0, 1, 2)

        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)

        self.lineEdit_Class_B = QLineEdit(self.frame_12)
        self.lineEdit_Class_B.setObjectName(u"lineEdit_Class_B")
        self.lineEdit_Class_B.setMinimumSize(QSize(0, 0))
        self.lineEdit_Class_B.setAlignment(Qt.AlignCenter)
        self.lineEdit_Class_B.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.lineEdit_Class_B, 5, 0, 1, 1)

        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 6, 0, 1, 2)

        self.label_24 = QLabel(self.frame_12)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 14, 0, 1, 2)

        self.lineEdit_Volume_B = QLineEdit(self.frame_12)
        self.lineEdit_Volume_B.setObjectName(u"lineEdit_Volume_B")
        self.lineEdit_Volume_B.setMinimumSize(QSize(0, 0))
        self.lineEdit_Volume_B.setAlignment(Qt.AlignCenter)
        self.lineEdit_Volume_B.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.lineEdit_Volume_B, 13, 0, 1, 1)

        self.lineEdit_Num_Sheets_B = QLineEdit(self.frame_12)
        self.lineEdit_Num_Sheets_B.setObjectName(u"lineEdit_Num_Sheets_B")
        self.lineEdit_Num_Sheets_B.setMinimumSize(QSize(0, 0))
        self.lineEdit_Num_Sheets_B.setAlignment(Qt.AlignCenter)
        self.lineEdit_Num_Sheets_B.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.lineEdit_Num_Sheets_B, 5, 1, 1, 1)

        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)

        self.lineEdit_Publisher_B = QLineEdit(self.frame_12)
        self.lineEdit_Publisher_B.setObjectName(u"lineEdit_Publisher_B")
        self.lineEdit_Publisher_B.setMinimumSize(QSize(0, 0))
        self.lineEdit_Publisher_B.setAlignment(Qt.AlignCenter)
        self.lineEdit_Publisher_B.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.lineEdit_Publisher_B, 3, 0, 1, 1)

        self.label_16 = QLabel(self.frame_12)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 4, 0, 1, 1)

        self.label_19 = QLabel(self.frame_12)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 4, 1, 1, 1)

        self.lineEdit_Year_E_B = QLineEdit(self.frame_12)
        self.lineEdit_Year_E_B.setObjectName(u"lineEdit_Year_E_B")
        self.lineEdit_Year_E_B.setMinimumSize(QSize(0, 0))
        self.lineEdit_Year_E_B.setMaxLength(4)
        self.lineEdit_Year_E_B.setCursorPosition(0)
        self.lineEdit_Year_E_B.setAlignment(Qt.AlignCenter)
        self.lineEdit_Year_E_B.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_Year_E_B.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.lineEdit_Year_E_B, 3, 1, 1, 1)

        self.textEdit_Details_B = QTextEdit(self.frame_12)
        self.textEdit_Details_B.setObjectName(u"textEdit_Details_B")
        self.textEdit_Details_B.setMinimumSize(QSize(0, 35))

        self.gridLayout_3.addWidget(self.textEdit_Details_B, 15, 0, 1, 2)


        self.gridLayout_4.addWidget(self.frame_12, 1, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.tab_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QWidget{	\n"
"	background-color: #cae8ff;\n"
"	color: Black;\n"
"}\n"
"QPushButton{\n"
"	color:#242424;\n"
"	text-align:center;\n"
"	height:30px;\n"
"	width:80px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.pushButton_Cad_B = QPushButton(self.frame_11)
        self.pushButton_Cad_B.setObjectName(u"pushButton_Cad_B")
        self.pushButton_Cad_B.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Cad_B.setStyleSheet(u"background-color: green;	\n"
"color: white;")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/mais.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Cad_B.setIcon(icon14)

        self.verticalLayout_11.addWidget(self.pushButton_Cad_B)

        self.line_2 = QFrame(self.frame_11)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_2)

        self.pushButton_Cancel_B = QPushButton(self.frame_11)
        self.pushButton_Cancel_B.setObjectName(u"pushButton_Cancel_B")
        self.pushButton_Cancel_B.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Cancel_B.setStyleSheet(u"background-color: red;	\n"
"color: white;")
        self.pushButton_Cancel_B.setIcon(icon)

        self.verticalLayout_11.addWidget(self.pushButton_Cancel_B)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_3.addWidget(self.tabWidget_2)

        self.stackedWidget.addWidget(self.page_Lib)
        self.page_Reader = QWidget()
        self.page_Reader.setObjectName(u"page_Reader")
        self.gridLayout_8 = QGridLayout(self.page_Reader)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.tabWidget = QTabWidget(self.page_Reader)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet(u"QTabBar::tab {\n"
"                width: 0px;  \n"
"                padding: 0px; \n"
"                margin: 0px; \n"
"            }")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QWidget{	\n"
"	background-color: #cae8ff;\n"
"	color: Black;\n"
"}\n"
"QPushButton{\n"
"	background-color: #5CE1E6;	\n"
"	color:#242424;\n"
"	border-radius:20px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 50))
        self.label_3.setMaximumSize(QSize(50, 50))
        self.label_3.setPixmap(QPixmap(u":/icons/icons/ler.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_3)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.pushButton_Refresh_Reader = QPushButton(self.frame_2)
        self.pushButton_Refresh_Reader.setObjectName(u"pushButton_Refresh_Reader")
        self.pushButton_Refresh_Reader.setMinimumSize(QSize(40, 40))
        self.pushButton_Refresh_Reader.setMaximumSize(QSize(40, 40))
        self.pushButton_Refresh_Reader.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Refresh_Reader.setIcon(icon9)
        self.pushButton_Refresh_Reader.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.pushButton_Refresh_Reader)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.tableWidget_Reader = QTableWidget(self.tab)
        if (self.tableWidget_Reader.columnCount() < 11):
            self.tableWidget_Reader.setColumnCount(11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_Reader.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_Reader.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_Reader.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_Reader.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_Reader.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_Reader.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_Reader.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_Reader.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_Reader.setHorizontalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_Reader.setHorizontalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_Reader.setHorizontalHeaderItem(10, __qtablewidgetitem22)
        self.tableWidget_Reader.setObjectName(u"tableWidget_Reader")

        self.verticalLayout_6.addWidget(self.tableWidget_Reader)

        self.frame_7 = QFrame(self.tab)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QWidget{	\n"
"	background-color: #cae8ff;\n"
"	color: Black;\n"
"}\n"
"QPushButton{\n"
"	background-color: #5CE1E6;	\n"
"	color:#242424;\n"
"	text-align:center;\n"
"	height:30px;\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_Cad_Reader_Page = QPushButton(self.frame_7)
        self.pushButton_Cad_Reader_Page.setObjectName(u"pushButton_Cad_Reader_Page")
        self.pushButton_Cad_Reader_Page.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Cad_Reader_Page.setStyleSheet(u"background-color: green;\n"
"color:white;	")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/adicionar-usuario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Cad_Reader_Page.setIcon(icon15)

        self.horizontalLayout_5.addWidget(self.pushButton_Cad_Reader_Page)

        self.line_7 = QFrame(self.frame_7)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_7)

        self.pushButton_Update_Reader = QPushButton(self.frame_7)
        self.pushButton_Update_Reader.setObjectName(u"pushButton_Update_Reader")
        self.pushButton_Update_Reader.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/carteira-de-identidade.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Update_Reader.setIcon(icon16)
        self.pushButton_Update_Reader.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_Update_Reader)

        self.line_8 = QFrame(self.frame_7)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_8)

        self.pushButton_Delete_Reader = QPushButton(self.frame_7)
        self.pushButton_Delete_Reader.setObjectName(u"pushButton_Delete_Reader")
        self.pushButton_Delete_Reader.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Delete_Reader.setStyleSheet(u"background-color: red;\n"
"color:white;	")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/deletar-usuario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Delete_Reader.setIcon(icon17)

        self.horizontalLayout_5.addWidget(self.pushButton_Delete_Reader)

        self.line_9 = QFrame(self.frame_7)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_9)

        self.pushButton_Export_Excel_Reader = QPushButton(self.frame_7)
        self.pushButton_Export_Excel_Reader.setObjectName(u"pushButton_Export_Excel_Reader")
        self.pushButton_Export_Excel_Reader.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Export_Excel_Reader.setIcon(icon13)

        self.horizontalLayout_5.addWidget(self.pushButton_Export_Excel_Reader)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_6 = QFrame(self.tab_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(420, 60))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(40, 40))
        self.label_8.setMaximumSize(QSize(40, 40))
        self.label_8.setPixmap(QPixmap(u":/icons/icons/adicionar-usuario.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_8)

        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 30))
        self.label_14.setMaximumSize(QSize(420, 30))

        self.horizontalLayout_14.addWidget(self.label_14)


        self.gridLayout_5.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(420, 16777215))
        self.frame_13.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(232, 230, 230);\n"
"height:40px;\n"
"border-radius:10px;\n"
"}\n"
"QLabel{\n"
"qproperty-alignment: 'AlignCenter';\n"
"}\n"
"QComboBox{\n"
"background-color: rgb(232, 230, 230);\n"
"height:40px;\n"
"border-radius:10px;\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_13)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_Tel_Reader = QLineEdit(self.frame_13)
        self.lineEdit_Tel_Reader.setObjectName(u"lineEdit_Tel_Reader")
        self.lineEdit_Tel_Reader.setMaxLength(15)
        self.lineEdit_Tel_Reader.setFrame(True)
        self.lineEdit_Tel_Reader.setEchoMode(QLineEdit.Normal)
        self.lineEdit_Tel_Reader.setCursorPosition(15)
        self.lineEdit_Tel_Reader.setAlignment(Qt.AlignCenter)
        self.lineEdit_Tel_Reader.setDragEnabled(False)
        self.lineEdit_Tel_Reader.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_Tel_Reader.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_Tel_Reader, 1, 1, 1, 1)

        self.lineEdit_Email_Reader = QLineEdit(self.frame_13)
        self.lineEdit_Email_Reader.setObjectName(u"lineEdit_Email_Reader")
        self.lineEdit_Email_Reader.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.lineEdit_Email_Reader.setAlignment(Qt.AlignCenter)
        self.lineEdit_Email_Reader.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_Email_Reader.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_Email_Reader, 3, 0, 1, 2)

        self.lineEdit_CEP_Reader = QLineEdit(self.frame_13)
        self.lineEdit_CEP_Reader.setObjectName(u"lineEdit_CEP_Reader")
        self.lineEdit_CEP_Reader.setAlignment(Qt.AlignCenter)
        self.lineEdit_CEP_Reader.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_CEP_Reader.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_CEP_Reader, 7, 0, 1, 2)

        self.lineEdit_Address_Reader = QLineEdit(self.frame_13)
        self.lineEdit_Address_Reader.setObjectName(u"lineEdit_Address_Reader")
        self.lineEdit_Address_Reader.setAlignment(Qt.AlignCenter)
        self.lineEdit_Address_Reader.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_Address_Reader, 12, 0, 1, 2)

        self.lineEdit_D_Cad_Reader = QLineEdit(self.frame_13)
        self.lineEdit_D_Cad_Reader.setObjectName(u"lineEdit_D_Cad_Reader")
        self.lineEdit_D_Cad_Reader.setCursorPosition(0)
        self.lineEdit_D_Cad_Reader.setAlignment(Qt.AlignCenter)
        self.lineEdit_D_Cad_Reader.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_D_Cad_Reader.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_D_Cad_Reader, 14, 0, 1, 2)

        self.lineEdit_Name_Reader = QLineEdit(self.frame_13)
        self.lineEdit_Name_Reader.setObjectName(u"lineEdit_Name_Reader")
        self.lineEdit_Name_Reader.setAlignment(Qt.AlignCenter)
        self.lineEdit_Name_Reader.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_Name_Reader.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_Name_Reader, 1, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_3)

        self.pushButton_Not_Cep = QPushButton(self.frame_13)
        self.pushButton_Not_Cep.setObjectName(u"pushButton_Not_Cep")
        self.pushButton_Not_Cep.setMaximumSize(QSize(150, 16777215))
        self.pushButton_Not_Cep.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Not_Cep.setStyleSheet(u"border: none; color:blue; text-decoration: underline;")

        self.horizontalLayout_16.addWidget(self.pushButton_Not_Cep)


        self.gridLayout_2.addLayout(self.horizontalLayout_16, 15, 0, 1, 2)

        self.label_29 = QLabel(self.frame_13)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 4, 1, 1, 1)

        self.lineEdit_CPF_Reader = QLineEdit(self.frame_13)
        self.lineEdit_CPF_Reader.setObjectName(u"lineEdit_CPF_Reader")
        self.lineEdit_CPF_Reader.setMaxLength(14)
        self.lineEdit_CPF_Reader.setCursorPosition(0)
        self.lineEdit_CPF_Reader.setAlignment(Qt.AlignCenter)
        self.lineEdit_CPF_Reader.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_CPF_Reader.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_CPF_Reader, 5, 0, 1, 1)

        self.lineEdit_Dn_Reader = QLineEdit(self.frame_13)
        self.lineEdit_Dn_Reader.setObjectName(u"lineEdit_Dn_Reader")
        self.lineEdit_Dn_Reader.setCursorPosition(0)
        self.lineEdit_Dn_Reader.setAlignment(Qt.AlignCenter)
        self.lineEdit_Dn_Reader.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_Dn_Reader.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_Dn_Reader, 9, 1, 1, 1)

        self.label_28 = QLabel(self.frame_13)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 4, 0, 1, 1)

        self.label_26 = QLabel(self.frame_13)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 0, 1, 1, 1)

        self.label_27 = QLabel(self.frame_13)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 2, 0, 1, 2)

        self.label_30 = QLabel(self.frame_13)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_2.addWidget(self.label_30, 6, 0, 1, 2)

        self.label_25 = QLabel(self.frame_13)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 0, 0, 1, 1)

        self.label_31 = QLabel(self.frame_13)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_2.addWidget(self.label_31, 8, 0, 1, 1)

        self.label_32 = QLabel(self.frame_13)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_2.addWidget(self.label_32, 8, 1, 1, 1)

        self.label_33 = QLabel(self.frame_13)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_2.addWidget(self.label_33, 11, 0, 1, 2)

        self.label_34 = QLabel(self.frame_13)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_2.addWidget(self.label_34, 13, 0, 1, 2)

        self.combo_Sc_Reader = QComboBox(self.frame_13)
        self.combo_Sc_Reader.addItem("")
        self.combo_Sc_Reader.addItem("")
        self.combo_Sc_Reader.addItem("")
        self.combo_Sc_Reader.addItem("")
        self.combo_Sc_Reader.addItem("")
        self.combo_Sc_Reader.addItem("")
        self.combo_Sc_Reader.addItem("")
        self.combo_Sc_Reader.setObjectName(u"combo_Sc_Reader")
        self.combo_Sc_Reader.setEditable(False)
        self.combo_Sc_Reader.setFrame(True)

        self.gridLayout_2.addWidget(self.combo_Sc_Reader, 9, 0, 1, 1)

        self.lineEdit_Ide_Reader = QLineEdit(self.frame_13)
        self.lineEdit_Ide_Reader.setObjectName(u"lineEdit_Ide_Reader")
        self.lineEdit_Ide_Reader.setMaxLength(11)
        self.lineEdit_Ide_Reader.setAlignment(Qt.AlignCenter)
        self.lineEdit_Ide_Reader.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_Ide_Reader.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_Ide_Reader, 5, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_13, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.tab_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(100, 16777215))
        self.frame_8.setStyleSheet(u"QWidget{	\n"
"	background-color: #cae8ff;\n"
"	color: Black;\n"
"}\n"
"QPushButton{\n"
"	color:#242424;\n"
"	text-align:center;\n"
"	height:30px;\n"
"	width:80px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.pushButton_Cad_Reader = QPushButton(self.frame_8)
        self.pushButton_Cad_Reader.setObjectName(u"pushButton_Cad_Reader")
        self.pushButton_Cad_Reader.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Cad_Reader.setStyleSheet(u"background-color: green;	\n"
"color: white;")
        self.pushButton_Cad_Reader.setIcon(icon14)

        self.verticalLayout_8.addWidget(self.pushButton_Cad_Reader)

        self.line_6 = QFrame(self.frame_8)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_6)

        self.pushButton_Cancel_Reader = QPushButton(self.frame_8)
        self.pushButton_Cancel_Reader.setObjectName(u"pushButton_Cancel_Reader")
        self.pushButton_Cancel_Reader.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Cancel_Reader.setStyleSheet(u"background-color: red;\n"
"color:white;	")
        self.pushButton_Cancel_Reader.setIcon(icon)

        self.verticalLayout_8.addWidget(self.pushButton_Cancel_Reader)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)


        self.horizontalLayout_8.addWidget(self.frame_8)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_Reader)
        self.page_Colab = QWidget()
        self.page_Colab.setObjectName(u"page_Colab")
        self.gridLayout_6 = QGridLayout(self.page_Colab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.tabWidget_3 = QTabWidget(self.page_Colab)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setStyleSheet(u"QTabBar::tab {\n"
"                width: 0px;  \n"
"                padding: 0px; \n"
"                margin: 0px; \n"
"            }")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_13 = QVBoxLayout(self.tab_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_3 = QFrame(self.tab_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QWidget{	\n"
"	background-color: #cae8ff;\n"
"	color: Black;\n"
"}\n"
"QPushButton{\n"
"	background-color: #5CE1E6;	\n"
"	color:#242424;\n"
"	border-radius:20px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 50))
        self.label_4.setMaximumSize(QSize(50, 50))
        self.label_4.setPixmap(QPixmap(u":/icons/icons/grupo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_4)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_12.addWidget(self.label_7)

        self.pushButton_Refresh_Colab = QPushButton(self.frame_3)
        self.pushButton_Refresh_Colab.setObjectName(u"pushButton_Refresh_Colab")
        self.pushButton_Refresh_Colab.setMinimumSize(QSize(40, 40))
        self.pushButton_Refresh_Colab.setMaximumSize(QSize(40, 40))
        self.pushButton_Refresh_Colab.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Refresh_Colab.setIcon(icon9)
        self.pushButton_Refresh_Colab.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.pushButton_Refresh_Colab)


        self.verticalLayout_13.addWidget(self.frame_3)

        self.tableWidget_Colab = QTableWidget(self.tab_5)
        if (self.tableWidget_Colab.columnCount() < 4):
            self.tableWidget_Colab.setColumnCount(4)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_Colab.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_Colab.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_Colab.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_Colab.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        self.tableWidget_Colab.setObjectName(u"tableWidget_Colab")
        self.tableWidget_Colab.setShowGrid(True)
        self.tableWidget_Colab.setSortingEnabled(False)

        self.verticalLayout_13.addWidget(self.tableWidget_Colab)

        self.frame_14 = QFrame(self.tab_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"QWidget{	\n"
"	background-color: #cae8ff;\n"
"	color: Black;\n"
"}\n"
"QPushButton{\n"
"	background-color: #5CE1E6;	\n"
"	color:#242424;\n"
"	text-align:center;\n"
"	height:30px;\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_Cad_Colab_Page = QPushButton(self.frame_14)
        self.pushButton_Cad_Colab_Page.setObjectName(u"pushButton_Cad_Colab_Page")
        self.pushButton_Cad_Colab_Page.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Cad_Colab_Page.setStyleSheet(u"background-color: green;\n"
"color:white;	")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/cedula.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Cad_Colab_Page.setIcon(icon18)

        self.horizontalLayout_7.addWidget(self.pushButton_Cad_Colab_Page)

        self.pushButton_Update_Colab = QPushButton(self.frame_14)
        self.pushButton_Update_Colab.setObjectName(u"pushButton_Update_Colab")
        self.pushButton_Update_Colab.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/editar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Update_Colab.setIcon(icon19)

        self.horizontalLayout_7.addWidget(self.pushButton_Update_Colab)

        self.pushButton_Delete_Colab = QPushButton(self.frame_14)
        self.pushButton_Delete_Colab.setObjectName(u"pushButton_Delete_Colab")
        self.pushButton_Delete_Colab.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Delete_Colab.setStyleSheet(u"background-color: red;\n"
"color:white;")
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/excluir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_Delete_Colab.setIcon(icon20)

        self.horizontalLayout_7.addWidget(self.pushButton_Delete_Colab)


        self.verticalLayout_13.addWidget(self.frame_14)

        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget_3.addTab(self.tab_6, "")

        self.gridLayout_6.addWidget(self.tabWidget_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_Colab)
        self.page_On = QWidget()
        self.page_On.setObjectName(u"page_On")
        self.gridLayout = QGridLayout(self.page_On)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.page_On)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_On)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_7 = QGridLayout(self.page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_5 = QWidget(self.page)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_16 = QFrame(self.widget_5)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_16)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalSpacer_4 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.label_35 = QLabel(self.frame_16)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(120, 120))
        self.label_35.setMaximumSize(QSize(120, 120))
        self.label_35.setPixmap(QPixmap(u":/icons/icons/perfil-de-usuario.png"))
        self.label_35.setScaledContents(True)

        self.gridLayout_14.addWidget(self.label_35, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.nome_edit = QLabel(self.frame_18)
        self.nome_edit.setObjectName(u"nome_edit")
        self.nome_edit.setGeometry(QRect(110, 30, 101, 31))
        self.nome_user_edit = QLabel(self.frame_18)
        self.nome_user_edit.setObjectName(u"nome_user_edit")
        self.nome_user_edit.setGeometry(QRect(110, 80, 101, 31))
        self.nome_user_edit_2 = QLabel(self.frame_18)
        self.nome_user_edit_2.setObjectName(u"nome_user_edit_2")
        self.nome_user_edit_2.setGeometry(QRect(110, 130, 101, 31))
        self.pushButton = QPushButton(self.frame_18)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 210, 75, 23))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border:None;\n"
"text-decorate:;\n"
"}")

        self.gridLayout_14.addWidget(self.frame_18, 1, 0, 1, 3)


        self.horizontalLayout_3.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.widget_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_17)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.stackedWidget_2 = QStackedWidget(self.frame_17)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget_2.addWidget(self.page_3)

        self.gridLayout_15.addWidget(self.stackedWidget_2, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_17)


        self.gridLayout_7.addWidget(self.widget_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)

        self.gridLayout_12.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_3, 0, 2, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget{	\n"
"	background-color: #cae8ff;\n"
"	color: Black;\n"
"}\n"
"QPushButton{\n"
"	color:Black;\n"
"	text-align:left;\n"
"	height:50px;\n"
"	border: none;\n"
"	padding-left:10px;\n"
"	padding-right:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:#5CE1E6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:#5CE1E6;\n"
"}\n"
"")
        self.gridLayout_10 = QGridLayout(self.widget_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(-1, -1, 0, -1)
        self.pushButton_ReturnConnect = QPushButton(self.widget_2)
        self.pushButton_ReturnConnect.setObjectName(u"pushButton_ReturnConnect")
        self.pushButton_ReturnConnect.setMinimumSize(QSize(30, 30))
        self.pushButton_ReturnConnect.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_ReturnConnect.setIcon(icon)
        self.pushButton_ReturnConnect.setIconSize(QSize(25, 25))

        self.gridLayout_10.addWidget(self.pushButton_ReturnConnect, 2, 0, 1, 1)

        self.Nav1 = QFrame(self.widget_2)
        self.Nav1.setObjectName(u"Nav1")
        self.Nav1.setFrameShape(QFrame.StyledPanel)
        self.Nav1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Nav1)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_home = QPushButton(self.Nav1)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_home.setIcon(icon1)
        self.pushButton_home.setIconSize(QSize(30, 30))
        self.pushButton_home.setCheckable(True)
        self.pushButton_home.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_home)

        self.pushButton_lib = QPushButton(self.Nav1)
        self.pushButton_lib.setObjectName(u"pushButton_lib")
        self.pushButton_lib.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_lib.setIcon(icon2)
        self.pushButton_lib.setIconSize(QSize(25, 25))
        self.pushButton_lib.setCheckable(True)
        self.pushButton_lib.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_lib)

        self.pushButton_reader = QPushButton(self.Nav1)
        self.pushButton_reader.setObjectName(u"pushButton_reader")
        self.pushButton_reader.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reader.setIcon(icon3)
        self.pushButton_reader.setIconSize(QSize(30, 30))
        self.pushButton_reader.setCheckable(True)
        self.pushButton_reader.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_reader)

        self.pushButton_colab = QPushButton(self.Nav1)
        self.pushButton_colab.setObjectName(u"pushButton_colab")
        self.pushButton_colab.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_colab.setIcon(icon4)
        self.pushButton_colab.setIconSize(QSize(40, 40))
        self.pushButton_colab.setCheckable(True)
        self.pushButton_colab.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_colab)

        self.pushButton_on = QPushButton(self.Nav1)
        self.pushButton_on.setObjectName(u"pushButton_on")
        self.pushButton_on.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_on.setIcon(icon5)
        self.pushButton_on.setIconSize(QSize(30, 30))
        self.pushButton_on.setCheckable(True)
        self.pushButton_on.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_on)


        self.gridLayout_10.addWidget(self.Nav1, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 292, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_home2.toggled.connect(self.pushButton_home.setChecked)
        self.pushButton_lib2.toggled.connect(self.pushButton_lib.setChecked)
        self.pushButton_reader2.toggled.connect(self.pushButton_reader.setChecked)
        self.pushButton_colab2.toggled.connect(self.pushButton_colab.setChecked)
        self.pushButton_home.toggled.connect(self.pushButton_home2.setChecked)
        self.pushButton_lib.toggled.connect(self.pushButton_lib2.setChecked)
        self.pushButton_reader.toggled.connect(self.pushButton_reader2.setChecked)
        self.pushButton_colab.toggled.connect(self.pushButton_colab2.setChecked)
        self.pushButton_Refresh_B.toggled.connect(self.tabWidget_2.update)
        self.pushButton_on.toggled.connect(self.pushButton_on2.setChecked)
        self.pushButton_on2.toggled.connect(self.pushButton_on.setChecked)
        self.pushButton_Menu.toggled.connect(self.widget.setHidden)
        self.pushButton_Menu.toggled.connect(self.widget_2.setVisible)

        self.stackedWidget.setCurrentIndex(5)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_Return_Connect2.setText("")
        self.pushButton_home2.setText("")
        self.pushButton_lib2.setText("")
        self.pushButton_reader2.setText("")
        self.pushButton_colab2.setText("")
        self.pushButton_on2.setText("")
        self.pushButton_Menu.setText("")
        self.pushButton_Perfil_Colab.setText("")
        self.input_Seach_Home.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquise aqui....", None))
        self.pushButton_Seach_Home.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Todos os direitos reservados a LIBRYNO - 2024 - <span style=\" color:#242424;\">Vers\u00e3o : 1.0</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.stackedWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">HOME</span></p></body></html>", None))
        self.label_2.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Livros</span></p></body></html>", None))
        self.pushButton_Refresh_B.setText("")
        ___qtablewidgetitem = self.tableWidget_B.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID_Livro", None));
        ___qtablewidgetitem1 = self.tableWidget_B.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Numero_Tombo", None));
        ___qtablewidgetitem2 = self.tableWidget_B.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ISBN", None));
        ___qtablewidgetitem3 = self.tableWidget_B.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Editora", None));
        ___qtablewidgetitem4 = self.tableWidget_B.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ano_Edicao", None));
        ___qtablewidgetitem5 = self.tableWidget_B.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Classificacao", None));
        ___qtablewidgetitem6 = self.tableWidget_B.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Numero_Folhas", None));
        ___qtablewidgetitem7 = self.tableWidget_B.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo do Livro", None));
        ___qtablewidgetitem8 = self.tableWidget_B.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        ___qtablewidgetitem9 = self.tableWidget_B.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Volume", None));
        ___qtablewidgetitem10 = self.tableWidget_B.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Data_Cadastro", None));
        ___qtablewidgetitem11 = self.tableWidget_B.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Assunto", None));
        self.pushButton_Cad_B_Page.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButton_Update_B.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.pushButton_Delete_B.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.pushButton_Export_Excel_B.setText(QCoreApplication.translate("MainWindow", u"Criar Excel", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_9.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Cadastrar Livro</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_D_Cad_B.setToolTip(QCoreApplication.translate("MainWindow", u"Data", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_D_Cad_B.setInputMask(QCoreApplication.translate("MainWindow", u"00/00/0000", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Num_Tombo_B.setToolTip(QCoreApplication.translate("MainWindow", u"Numeros", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_Num_Tombo_B.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_Num_Tombo_B.setPlaceholderText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Editora:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_ISBM_B.setToolTip(QCoreApplication.translate("MainWindow", u"Numeros", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_ISBM_B.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ano da Edi\u00e7\u00e3o:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Volume:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Title_B.setToolTip(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Title_B.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_Name_A_B.setToolTip(QCoreApplication.translate("MainWindow", u"Texto", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Name_A_B.setPlaceholderText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Data de Cadastro:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Nome do Autor:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Numero Tombo:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Class_B.setToolTip(QCoreApplication.translate("MainWindow", u"Texto", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Class_B.setPlaceholderText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo do Livro:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Assunto:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Volume_B.setToolTip(QCoreApplication.translate("MainWindow", u"Numeros", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Volume_B.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_Num_Sheets_B.setToolTip(QCoreApplication.translate("MainWindow", u"Numeros", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Num_Sheets_B.setPlaceholderText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ISBN:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Publisher_B.setToolTip(QCoreApplication.translate("MainWindow", u"Texto", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Publisher_B.setPlaceholderText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Classifica\u00e7\u00e3o:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Numero de Folhas:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Year_E_B.setToolTip(QCoreApplication.translate("MainWindow", u"Data", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Year_E_B.setInputMask("")
        self.lineEdit_Year_E_B.setPlaceholderText("")
        self.pushButton_Cad_B.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButton_Cancel_B.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Leitores</span></p></body></html>", None))
        self.pushButton_Refresh_Reader.setText("")
        ___qtablewidgetitem12 = self.tableWidget_Reader.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ID_Leitor", None));
        ___qtablewidgetitem13 = self.tableWidget_Reader.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem14 = self.tableWidget_Reader.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem15 = self.tableWidget_Reader.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem16 = self.tableWidget_Reader.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem17 = self.tableWidget_Reader.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Identidade", None));
        ___qtablewidgetitem18 = self.tableWidget_Reader.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem19 = self.tableWidget_Reader.horizontalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Escolaridade", None));
        ___qtablewidgetitem20 = self.tableWidget_Reader.horizontalHeaderItem(8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Data_Nascimento", None));
        ___qtablewidgetitem21 = self.tableWidget_Reader.horizontalHeaderItem(9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem22 = self.tableWidget_Reader.horizontalHeaderItem(10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Data_Cadastro", None));
        self.pushButton_Cad_Reader_Page.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButton_Update_Reader.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.pushButton_Delete_Reader.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.pushButton_Export_Excel_Reader.setText(QCoreApplication.translate("MainWindow", u"Criar Excel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_8.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Cadastrar Leitor</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Tel_Reader.setToolTip(QCoreApplication.translate("MainWindow", u"Numeros", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Tel_Reader.setInputMask(QCoreApplication.translate("MainWindow", u"(99) 99999-9999", None))
        self.lineEdit_Tel_Reader.setText(QCoreApplication.translate("MainWindow", u"() -", None))
        self.lineEdit_Tel_Reader.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_Email_Reader.setToolTip(QCoreApplication.translate("MainWindow", u"Texto", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Email_Reader.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_CEP_Reader.setToolTip(QCoreApplication.translate("MainWindow", u"Numeros", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_CEP_Reader.setInputMask(QCoreApplication.translate("MainWindow", u"00000-000", None))
        self.lineEdit_CEP_Reader.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_Address_Reader.setToolTip(QCoreApplication.translate("MainWindow", u"Texto", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Address_Reader.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_D_Cad_Reader.setToolTip(QCoreApplication.translate("MainWindow", u"Data", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_D_Cad_Reader.setInputMask(QCoreApplication.translate("MainWindow", u"00/00/0000", None))
        self.lineEdit_D_Cad_Reader.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_Name_Reader.setToolTip(QCoreApplication.translate("MainWindow", u"Texto", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Name_Reader.setPlaceholderText("")
        self.pushButton_Not_Cep.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o sei meu CEP", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Identidade:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_CPF_Reader.setToolTip(QCoreApplication.translate("MainWindow", u"Numeros", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_CPF_Reader.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000-00", None))
        self.lineEdit_CPF_Reader.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_Dn_Reader.setToolTip(QCoreApplication.translate("MainWindow", u"Data", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Dn_Reader.setInputMask(QCoreApplication.translate("MainWindow", u"00/00/0000", None))
        self.lineEdit_Dn_Reader.setPlaceholderText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"CEP:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Escolaridade:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Data de Cadastro:", None))
        self.combo_Sc_Reader.setItemText(0, "")
        self.combo_Sc_Reader.setItemText(1, QCoreApplication.translate("MainWindow", u"Fundamental-Incompleto", None))
        self.combo_Sc_Reader.setItemText(2, QCoreApplication.translate("MainWindow", u"Fundamental-Completo", None))
        self.combo_Sc_Reader.setItemText(3, QCoreApplication.translate("MainWindow", u"Medio-Cursando", None))
        self.combo_Sc_Reader.setItemText(4, QCoreApplication.translate("MainWindow", u"Medio-Completo", None))
        self.combo_Sc_Reader.setItemText(5, QCoreApplication.translate("MainWindow", u"Superior-Cursando", None))
        self.combo_Sc_Reader.setItemText(6, QCoreApplication.translate("MainWindow", u"Superior-Completo", None))

#if QT_CONFIG(tooltip)
        self.combo_Sc_Reader.setToolTip(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.combo_Sc_Reader.setCurrentText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_Ide_Reader.setToolTip(QCoreApplication.translate("MainWindow", u"Numeros", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Ide_Reader.setPlaceholderText("")
        self.pushButton_Cad_Reader.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButton_Cancel_Reader.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_4.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Colaboradores</span></p></body></html>", None))
        self.pushButton_Refresh_Colab.setText("")
        ___qtablewidgetitem23 = self.tableWidget_Colab.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"ID_Colaborador", None));
        ___qtablewidgetitem24 = self.tableWidget_Colab.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Nome_Colaborador", None));
        ___qtablewidgetitem25 = self.tableWidget_Colab.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Usuario_de_login", None));
        ___qtablewidgetitem26 = self.tableWidget_Colab.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Senha_de usuario", None));
        self.pushButton_Cad_Colab_Page.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButton_Update_Colab.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.pushButton_Delete_Colab.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Page", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">SOBRE</span></p></body></html>", None))
        self.label_35.setText("")
        self.nome_edit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">NOME</p></body></html>", None))
        self.nome_user_edit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">NOME USUARIO</p></body></html>", None))
        self.nome_user_edit_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SENHA</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_ReturnConnect.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
        self.pushButton_home.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.pushButton_lib.setText(QCoreApplication.translate("MainWindow", u"BIBLIOTECA", None))
        self.pushButton_reader.setText(QCoreApplication.translate("MainWindow", u"LEITORES", None))
        self.pushButton_colab.setText(QCoreApplication.translate("MainWindow", u"COLABORADORES", None))
        self.pushButton_on.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
    # retranslateUi

