import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic

form_class = uic.loadUiType(r"C:\Users\crebi\Documents\GitHub\PyQt5\Exchanger\04_Exchange\exchanger.ui")[0]

class WindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_Open.triggered.connect(self.openFunction)
        self.action_Save.triggered.connect(self.saveFunction)
        self.pushButton_Clear.clicked.connect(self.clearFunction)
        self.pushButton_Exec.clicked.connect(self.execFunction)
        self.pushButton_Copy.clicked.connect(self.copyFunction)
        self.pushButton_Exit.clicked.connect(self.exitFunction)

        self.strData = ''
        self.lstStrings = []
        self.lstLine = []
        self.lstDisplay = []

    def openFunction(self):
        print("Open!!!")
    
    def saveFunction(self):
        print("Save!!!")
        
    def clearFunction(self):
        print("Clear!")
        self.plainTextEdit_In.clear()
        self.plainTextEdit_Out.clear()

    def ErrorCheck(self):
        if self.strData == "":  
            print('Error!')
            self.strData = 'Error!'
        else:
            print('Execute!')
    
    def DataClear(self):
        self.lstLine = []
        self.lstStrings = []
        self.lstDisplay = []
        self.plainTextEdit_Out.clear()
        print("Clear!")
        pass

    def execFunction(self):
        paragraph = 0
        # Data Clear
        self.DataClear()
        
        # Data Input
        self.strData = self.plainTextEdit_In.toPlainText()
        
        # Error Check
        self.ErrorCheck()
       
        # Parsing
        self.lstLine = self.strData.split('\n')
        for i in self.lstLine:
            if i == '' and paragraph == 1:
                break
            elif i == '':
                paragraph = 1
                self.lstStrings.append(',')
            else:
                paragraph = 0
                self.lstStrings.append(i)
        
        text = " ".join(self.lstStrings)
        conditions = text.split(',')
        
        # Exchange
        seqs = []; conds = []; outs = []
        for i in conditions:
            seq = i.partition('.')[0]
            cond = i.partition('.')[2]    
            out = i.partition('/')[2]
            
            seqs.append(seq); conds.append(cond); outs.append(out)
        del seqs[-1]; del conds[-1]; del outs[-1]
        print(seq, seqs)
        # Display
        for i in range(len(seqs)):
            self.strOutput = '//' + seqs[i] + '\n' + conds[i] + '\n' + outs[i] + '\n'
            self.lstDisplay.append(self.strOutput)

        text = " ".join(self.lstDisplay)
        self.plainTextEdit_Out.setPlainText(text)

    def copyFunction(self):
        print("Copy!")
        self.plainTextEdit_Out.selectAll()
        self.plainTextEdit_Out.copy()

    def exitFunction(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", 
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print("Closed!")
            sys.exit()
        else:
            print("Not Closed!")
        
app = QtWidgets.QApplication(sys.argv)
mainwindow = WindowClass()
mainwindow.show()
app.exec_()
