import sys
import pyperclip
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic

form_class = uic.loadUiType(r"C:\Users\crebi\Documents\GitHub\PyQt5\Exchanger\05_Copy\exchanger.ui")[0]

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
            self.strData = 'Error!'
            reply = QMessageBox.information(self, 'Error', "There is no input.", QMessageBox.Ok, QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                print('Error!')
        else:
            print('Execute!')
    
    def DataClear(self):
        self.lstStrings = []
        self.lstDisplay = []
        self.plainTextEdit_Out.clear()
        print("Clear!")

    def execFunction(self):
        paragraph = 0
        # Data Clear
        self.DataClear()
        
        # Data Input
        self.strData = self.plainTextEdit_In.toPlainText()
        
        # Error Check
        self.ErrorCheck()
       
        # Data Parsing
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
        
        # Partitioning
        seqs = []; conds = []; outs = []
        for i in conditions:
            seq = i.partition('.')[0]
            cond = i.partition('.')[2].partition('/')[0]   
            out = i.partition('/')[2]
            
            seqs.append(seq); conds.append(cond); outs.append(out)
        del seqs[-1]; del conds[-1]; del outs[-1]
        
        # Event Handling
        for i in range(len(conds)):
            event = conds[i]
            if '@' in event:
                conds[i] = event.replace('@', 'Event_')

        # Disply
        for i in range(len(seqs)):
            if seqs[i] == 1:
                temp = 'if'
            else: 
                temp = 'else if'
            conds[i] = temp + '(' + conds[i] + ')'
            conds[i] = conds[i].replace('(', '((')
            conds[i] = conds[i].replace(')', '))')
            conds[i] = conds[i].replace('&&', ') && (')
            conds[i] = conds[i].replace('||', ') || (')

            if conds[i].count('(') != conds[i].count(')'):
                reply = QMessageBox.information(self, 'Error', 
                "The condition {} has error.".format(seqs[i]), QMessageBox.Ok, QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    print('Condition Error!')

            operator = '&'
            if conds[i].count(operator) % 2 != 0:
                reply = QMessageBox.information(self, 'Error', 
                "The operator({}) of condition{} have one or more errors.".format(operator, seqs[i]), QMessageBox.Ok, QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    print('Operator {} Error!'.format(operator))

            operator = '|'
            if conds[i].count(operator) % 2 != 0:
                reply = QMessageBox.information(self, 'Error', 
                "The operator({}) of condition{} have one or more errors.".format(operator, seqs[i]), QMessageBox.Ok, QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    print('Operator {} Error!'.format(operator))

            operator = '='
            if conds[i].count(operator) % 2 != 0:
                reply = QMessageBox.information(self, 'Error', 
                "The operator({}) of condition{} have one or more errors.".format(operator, seqs[i]), QMessageBox.Ok, QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    print('Operator {} Error!'.format(operator))

            outs[i] = outs[i].replace('/','\n')
            outs[i] = '{\n' + outs[i] + '\n}'

            self.strOutput = '//' + seqs[i] + '\n' + conds[i] + '\n' + outs[i] + '\n'
            self.lstDisplay.append(self.strOutput)

        text = " ".join(self.lstDisplay)
        self.plainTextEdit_Out.setPlainText(text)

    def copyFunction(self):
        print("Copy!")
        self.plainTextEdit_Out.selectAll()
        self.plainTextEdit_Out.copy()
        temp = self.plainTextEdit_Out.toPlainText()
        print(temp)
        pyperclip.copy(temp)

    def exitFunction(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", 
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print("Closed!")
            sys.exit()
        else:
            print("Not Closed!")

if __name__ == '__main__':      
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = WindowClass()
    mainwindow.show()
    app.exec_()
