import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r"C:\Users\crebi\Documents\GitHub\PyQt5\Designer\4_Notepad_OpenSave\notepad.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)

    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]:
            with open(fname[0], encoding = 'UTF8') as f:
                data = f.read()
            self.plainTextEdit.setPlainText(data)
            print("Open {}".format(fname[0]))
    
    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self)
        if fname[0]:
            data = self.plainTextEdit.toPlainText()

            with open(fname[0], 'w', encoding = 'UTF8') as f:
                f.write(data)
            print("Save {}".format(fname[0]))
    
app = QApplication(sys.argv)
mainwindow = WindowClass()
mainwindow.show()
app.exec_()