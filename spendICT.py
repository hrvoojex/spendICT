#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Calculating ICT costs
Author: Hrvoje T.
Last edited: July, 2017.
"""

import sys
from spendICT_gui import Ui_MainWindow
from PyQt5 import QtWidgets


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

