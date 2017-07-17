#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Calculating ICT expenses"""

from spendICT_gui import Ui_MainWindow
import sys
from PyQt5 import QtWidgets


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        # Action when some button is pressed
        self.pushButton_3.clicked.connect(self.writeToTextEdit)
        self.toolButton.clicked.connect(self.selectFile)
        self.toolButton_2.clicked.connect(self.selectFile)
        self.toolButton_3.clicked.connect(self.selectFile)
        self.pushButton_5.clicked.connect(self.odustaniClicked)

        # Declaring instance attributes
        self.listaFile = None
        self.specifikacijaFile = None
        self.adresarFile = None

        # Radio button default checked
        self.radioButton_2.setChecked(True)
        self.lineEdit_4.setDisabled(True)

    def writeToTextEdit(self):
        """Write a text in a textEdit"""
        self.listaFile = self.lineEdit_5.text()
        self.specifikacijaFile = self.lineEdit_6.text()
        self.adresarFile = self.lineEdit_7.text()
        self.textEdit.setText(
            self.listaFile + "\n" + self.specifikacijaFile + "\n" + self.adresarFile)

    def selectFile(self, event=None):
        """
        Opens a dialog for choosing a file. Takes two positionals arguments
        'self' and 'event' because 'mouseReleaseEvent' sends two, if using
        eg. 'label1.mouseReleaseEvent = self.showText1'.

        When subclassing QLineEdit as ClickableLineEdit 'event' is None"
        """
        # QFileDialog doesn't use native OS dialog like this one:
        # 'fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')'
        # to remember last opening path
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open File', '', 'Text file (*.csv)', None,
            QtWidgets.QFileDialog.DontUseNativeDialog)
        # sender is object that sends the signal
        sender = self.sender()
        # set options for combobox only from 'lista_lineEdit' QLineEdit widget
        if sender.objectName() == "toolButton":
            self.lineEdit_5.setText(fname)
        elif sender.objectName() == "toolButton_2":
            self.lineEdit_6.setText(fname)
        else:
            self.lineEdit_7.setText(fname)

    def odustaniClicked(self):
        self.listaFile = None
        self.specifikacijaFile = None
        self.adresarFile = None

        self.lineEdit_5.setText(self.listaFile)
        self.lineEdit_6.setText(self.specifikacijaFile)
        self.lineEdit_7.setText(self.adresarFile)
        self.textEdit.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec_())