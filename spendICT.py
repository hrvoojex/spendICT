# -*- coding: utf-8 -*-
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

        # Declaring instance attributes
        self.listaFile = None

        # Radio button default checked
        self.radioButton_2.setChecked(True)
        self.lineEdit_4.setDisabled(True)

    def writeToTextEdit(self):
        """Write a text in a textEdit"""
        self.listaFile = self.lineEdit_5.text()
        self.textEdit.setText(self.listaFile)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec_())