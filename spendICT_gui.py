# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spendICT_gui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 351, 211))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(96, 32, 135, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(96, 70, 135, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(96, 108, 135, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(58, 32, 32, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(12, 70, 78, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(38, 108, 52, 18))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(11, 147, 84, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(125, 147, 84, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 351, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 150, 84, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 150, 84, 34))
        self.pushButton_5.setObjectName("pushButton_5")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 33, 311, 110))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 20, 401, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 351, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 101, 21))
        self.label_4.setObjectName("label_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(21, 100, 250, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 150, 287, 36))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 260, 771, 271))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 751, 231))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        self.menuMobiteli = QtWidgets.QMenu(self.menuMode)
        self.menuMobiteli.setObjectName("menuMobiteli")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionProgram = QtWidgets.QAction(MainWindow)
        self.actionProgram.setObjectName("actionProgram")
        self.actionIzlaz = QtWidgets.QAction(MainWindow)
        self.actionIzlaz.setObjectName("actionIzlaz")
        self.actionFiksni = QtWidgets.QAction(MainWindow)
        self.actionFiksni.setObjectName("actionFiksni")
        self.actionO_programu = QtWidgets.QAction(MainWindow)
        self.actionO_programu.setObjectName("actionO_programu")
        self.actionVIP = QtWidgets.QAction(MainWindow)
        self.actionVIP.setObjectName("actionVIP")
        self.menuFile.addAction(self.actionProgram)
        self.menuFile.addAction(self.actionIzlaz)
        self.menuMobiteli.addAction(self.actionVIP)
        self.menuMode.addAction(self.menuMobiteli.menuAction())
        self.menuMode.addAction(self.actionFiksni)
        self.menuAbout.addAction(self.actionO_programu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "spendICT"))
        self.groupBox.setTitle(_translate("MainWindow", "Unos podataka: "))
        self.label.setText(_translate("MainWindow", "Lista:"))
        self.label_2.setText(_translate("MainWindow", "Specifikacija:"))
        self.label_3.setText(_translate("MainWindow", "Adresar:"))
        self.pushButton.setText(_translate("MainWindow", "Prihvati"))
        self.pushButton_2.setText(_translate("MainWindow", "Odustani"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Unos podataka: "))
        self.pushButton_3.setText(_translate("MainWindow", "Prihvati"))
        self.pushButton_5.setText(_translate("MainWindow", "Odustani"))
        self.label_7.setText(_translate("MainWindow", "Lista:"))
        self.label_8.setText(_translate("MainWindow", "Specifikacija:"))
        self.label_9.setText(_translate("MainWindow", "Adresar:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Izlazni podaci"))
        self.label_4.setText(_translate("MainWindow", "Ciljani podatak"))
        self.label_5.setText(_translate("MainWindow", "Koliko brojeva:"))
        self.radioButton.setText(_translate("MainWindow", "Samo &jedan"))
        self.radioButton_2.setText(_translate("MainWindow", "Svi"))
        self.label_6.setText(_translate("MainWindow", "Koji broj:"))
        self.pushButton_4.setText(_translate("MainWindow", "Prihvati"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Prikaz"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuMode.setTitle(_translate("MainWindow", "Mo&de"))
        self.menuMobiteli.setTitle(_translate("MainWindow", "&Mobiteli"))
        self.menuAbout.setTitle(_translate("MainWindow", "Abo&ut"))
        self.actionProgram.setText(_translate("MainWindow", "&Program"))
        self.actionIzlaz.setText(_translate("MainWindow", "&Izlaz"))
        self.actionFiksni.setText(_translate("MainWindow", "&Fiksni"))
        self.actionO_programu.setText(_translate("MainWindow", "&O programu"))
        self.actionVIP.setText(_translate("MainWindow", "&VIP"))

