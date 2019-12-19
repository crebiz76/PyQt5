import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r"C:\Users\crebi\Documents\GitHub\PyQt5\Calculator\03_Calc_UI\Calc.ui")[0]

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
        self.lineEdit_input.textChanged.connect(self.lineEditChanged)

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        # Function
        # self.inval = inval
        # self.OpDisp = self.OperatorDisplay(self)
        # self.NumDisp = self.NumberDisplay(self)
        self.operate = True

    def OperatorDisplay(self, inval):
        self.inVal = inval
        if self.lineEdit_input.text() and self.operate == False:
            self.lineEdit_input.setText(self.lineEdit_input.text() + self.inVal)
            self.operate = True
            print(self.inVal, self.operate)

    def NumberDisplay(self, inval):
        self.inVal = inval
        if self.inVal == '0':
            if self.operate == False:
                self.lineEdit_input.setText(self.lineEdit_input.text() + self.inVal)
                self.operate = False
                print(self.inVal, self.operate)
        else:
            self.lineEdit_input.setText(self.lineEdit_input.text() + self.inVal)
            self.operate = False
            print(self.inVal, self.operate)

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

    def InputButton_equal(self):        
        print("equal")
        self.OperatorDisplay('=')
        
    def InputButton_plus(self): 
        print("plus")
        self.OperatorDisplay('+')        

    def InputButton_minus(self):
        print("minus")
        self.OperatorDisplay('-')
        
    def InputButton_multiply(self):
        print("multiply")
        self.OperatorDisplay('×')
        
    def InputButton_division(self):
        print("division")
        self.OperatorDisplay('÷')
        
    def InputButton_BS(self):   print("BS")
    def InputButton_C(self):    print("C")
    def InputButton_CE(self):   print("CE")

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit_input.text())

if __name__ == "__main__":
    App = QApplication(sys.argv)
    MainWindow = WindowClass()
    MainWindow.show()
    App.exec_()