import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r"C:\Users\crebi\Documents\GitHub\PyQt5\Calculator\01_Calc_Layout\Calc.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

App = QApplication(sys.argv)
MainWindow = WindowClass()
MainWindow.show()
App.exec_()