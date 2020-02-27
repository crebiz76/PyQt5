import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

form_class = uic.loadUiType(r"C:\Users\crebi\Documents\GitHub\PyQt5\Exchanger\02_Button\exchanger.ui")[0]

class WindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fontSize = 20

        self.action_Open.triggered.connect(self.openFunction)
        self.action_Save.triggered.connect(self.saveFunction)
        self.pushButton_Clear.clicked.connect(self.clearFunction)
        self.pushButton_Exec.clicked.connect(self.execFunction)
        self.pushButton_Copy.clicked.connect(self.copyFunction)

    def openFunction(self):
        print("Open!!!")
    
    def saveFunction(self):
        print("Save!!!")
        
    def clearFunction(self):
        print("Clear!")
        # self.plainTextEdit_In.setPlainText("")
        # self.plainTextEdit_Out.setPlainText("")
        self.plainTextEdit_In.clear()
        self.plainTextEdit_Out.clear()
    
    def execFunction(self):
        data = self.plainTextEdit_In.toPlainText()
        print("Clear!")
        # Error Check
        if data == "":  
            print('Error!')
            data = 'Error!'
        else:
            print('Execute!')
            
        # Exchange Data        
        self.plainTextEdit_Out.setPlainText(data)

    def copyFunction(self):
        print("Copy!")
        self.plainTextEdit_Out.selectAll()
        self.plainTextEdit_Out.copy()
        
app = QtWidgets.QApplication(sys.argv)
mainwindow = WindowClass()
mainwindow.show()
app.exec_()
