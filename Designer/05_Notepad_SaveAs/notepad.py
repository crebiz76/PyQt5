import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r"C:\Users\crebi\Documents\GitHub\PyQt5\Designer\05_Notepad_SaveAs\notepad.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        self.action_saveAs.triggered.connect(self.saveAsFunction)

        self.opened = False
        self.opened_filepath = ''        

    def open_file(self, fname):
        with open(fname, encoding = 'UTF8') as f:
            data = f.read()
        self.plainTextEdit.setPlainText(data)
        
        self.opened = True
        self.opened_filepath = fname

        print("Open {}".format(fname))

    def save_file(self, fname):
        data = self.plainTextEdit.toPlainText()
        with open(fname, 'w', encoding = 'UTF8') as f:
            f.write(data)

        self.opened = True
        self.opened_filepath = fname

        print("Save {}".format(fname))
    
    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]:
            self.open_file(fname[0])

    def saveFunction(self):
        if self.opened:
            self.save_file(self.opened_filepath)
        else:
            self.saveAsFunction()
    
    def saveAsFunction(self):
        fname = QFileDialog.getSaveFileName(self)
        if fname[0]:
            self.save_file(fname[0])
    
app = QApplication(sys.argv)
mainwindow = WindowClass()
mainwindow.show()
app.exec_()