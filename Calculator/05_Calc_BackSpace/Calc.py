import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r"C:\Users\crebi\Documents\GitHub\PyQt5\Calculator\05_Calc_BackSpace\Calc.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_0.clicked.connect(self.InputButton_0)
        self.btn_1.clicked.connect(self.InputButton_1)
        self.btn_2.clicked.connect(self.InputButton_2)
        self.btn_3.clicked.connect(self.InputButton_3)
        self.btn_4.clicked.connect(self.InputButton_4)
        self.btn_5.clicked.connect(self.InputButton_5)
        self.btn_6.clicked.connect(self.InputButton_6)
        self.btn_7.clicked.connect(self.InputButton_7)
        self.btn_8.clicked.connect(self.InputButton_8)
        self.btn_9.clicked.connect(self.InputButton_9)
        
        self.btn_point.clicked.connect(self.InputButton_point)
        self.btn_sign.clicked.connect(self.InputButton_sign)
        
        self.btn_equal.clicked.connect(self.InputButton_equal)
        
        self.btn_plus.clicked.connect(self.InputButton_plus)
        self.btn_minus.clicked.connect(self.InputButton_minus)
        self.btn_multiply.clicked.connect(self.InputButton_multiply)
        self.btn_division.clicked.connect(self.InputButton_division)

        self.btn_BS.clicked.connect(self.InputButton_BS)
        self.btn_C.clicked.connect(self.InputButton_C)
        self.btn_CE.clicked.connect(self.InputButton_CE)

        # LineEdit
        self.lineEdit_input.textChanged.connect(self.lineEdit_inputChanged)
        self.lineEdit_result.textChanged.connect(self.lineEdit_resultChanged)

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        # Initialization
        self.operate = True
        self.result = 0
        self.operand = 0
        self.op_pre = '+'
        self.point = False

    def OperatorDisplay(self, inval):
        self.inVal = inval
        if self.operate == False:
            if self.lineEdit_result.text():
                if self.point == True:  self.operand = float(self.lineEdit_result.text())
                else:                   self.operand = int(self.lineEdit_result.text())

                if self.op_pre == '+':      self.result = self.result + self.operand
                elif self.op_pre == '-':    self.result = self.result - self.operand
                elif self.op_pre == '×':    self.result = self.result * self.operand
                elif self.op_pre == '÷':    self.result = self.result / self.operand        
                self.op_pre = self.inVal

                self.lineEdit_input.setText(self.lineEdit_input.text() + self.lineEdit_result.text() + self.inVal)
                self.ResultDisplay()

                self.operate = True
                print(self.inVal, self.operate)
            
    def NumberDisplay(self, inval):
        self.inVal = inval
        if self.operate == False:
            self.lineEdit_result.setText(self.lineEdit_result.text() + self.inVal)
            self.operate = False
        else:   # self.operate == True
            if self.op_pre == '=':
                self.Clear()
            
            if self.inVal != '0':
                self.lineEdit_result.setText('')
                self.lineEdit_result.setText(self.inVal)
                self.operate = False            

    def keyReleaseEvent(self, e): 
        print(self.lineEdit_input.text())

    def InputButton_0(self):    self.NumberDisplay('0')
    def InputButton_1(self):    self.NumberDisplay('1')
    def InputButton_2(self):    self.NumberDisplay('2')
    def InputButton_3(self):    self.NumberDisplay('3')    
    def InputButton_4(self):    self.NumberDisplay('4')    
    def InputButton_5(self):    self.NumberDisplay('5')    
    def InputButton_6(self):    self.NumberDisplay('6')    
    def InputButton_7(self):    self.NumberDisplay('7')
    def InputButton_8(self):    self.NumberDisplay('8')  
    def InputButton_9(self):    self.NumberDisplay('9')
  
    def InputButton_point(self):   print("point")
    def InputButton_sign(self):    print("sign")

    def InputButton_equal(self):    self.OperatorDisplay('=')
    def InputButton_plus(self):     self.OperatorDisplay('+')        
    def InputButton_minus(self):    self.OperatorDisplay('-')
    def InputButton_multiply(self): self.OperatorDisplay('×')
    def InputButton_division(self): self.OperatorDisplay('÷')
        
    def InputButton_BS(self):
        self.BackSpace()

    def InputButton_C(self):
        self.Clear()
        
    def InputButton_CE(self):
        self.ClearEntity()

    def lineEdit_inputChanged(self):
        self.statusBar.showMessage(self.lineEdit_input.text())

    def lineEdit_resultChanged(self):
        self.statusBar.showMessage(self.lineEdit_input.text())

    def ResultDisplay(self):
        self.lineEdit_result.setText(str(self.result))

    def Clear(self):
        # Initialization
        self.operate = True
        self.result = 0
        self.operand = 0
        self.op_pre = '+'
        self.point = False
        self.ResultDisplay()
        self.lineEdit_input.setText('')

    def ClearEntity(self):
        self.operate = True
        self.lineEdit_result.setText('0')

    def BackSpace(self):
        if self.operate == False:
            if len(self.lineEdit_result.text()) == 1:
                self.ClearEntity()
            else:
                self.lineEdit_result.setText(self.lineEdit_result.text()[:-1])
        else:
            if self.op_pre == '=':
                self.lineEdit_input.setText('')
            

if __name__ == "__main__":
    App = QApplication(sys.argv)
    MainWindow = WindowClass()
    MainWindow.show()
    App.exec_()