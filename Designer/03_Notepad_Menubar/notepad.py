import sys
# from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import uic

form_class = uic.loadUiType(r"C:\Users\crebi\Documents\GitHub\PyQt5\Designer\03_Notepad_Menubar\notepad.ui")[0]

class WindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)

    def openFunction(self):
        print("Open!!!")
    
    def saveFunction(self):
        print("Save!!!")

app = QtWidgets.QApplication(sys.argv)
mainwindow = WindowClass()
mainwindow.show()
app.exec_()