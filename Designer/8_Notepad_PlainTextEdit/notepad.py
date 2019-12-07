import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r"C:\Users\crebi\Documents\GitHub\PyQt5\Designer\8_Notepad_PlainTextEdit\notepad.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        self.action_saveAs.triggered.connect(self.saveAsFunction)
        self.action_close.triggered.connect(self.close)

        self.action_undo.triggered.connect(self.undoFunction)
        self.action_cut.triggered.connect(self.cutFunction)
        self.action_copy.triggered.connect(self.copyFunction)
        self.action_paste.triggered.connect(self.pasteFunction)

        self.opened = False
        self.opened_filepath = ''

    def save_changed_data(self):
        msgBox = QMessageBox()
        msgBox.setText("변경내용을 {}에 저장하시겠습니까?".format(self.opened_filepath))
        msgBox.addButton("저장", QMessageBox.YesRole)
        msgBox.addButton("저장 안 함", QMessageBox.NoRole)
        msgBox.addButton("취소", QMessageBox.RejectRole)
        ret = msgBox.exec_()
        if ret == 0: print("Yes Button")
        elif ret == 1: print("No Button")
        elif ret == 2: print("Cancel Button"); return ret
        
    def closeEvent(self, event):
        ret = self.save_changed_data()
        if ret == 2: event.ignore()
        print("Close event")
        
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
    
    def undoFunction(self):
        self.plainTextEdit.undo()

    def cutFunction(self):
        self.plainTextEdit.cut()

    def copyFunction(self):
        self.plainTextEdit.copy()

    def pasteFunction(self):
        self.plainTextEdit.paste()

app = QApplication(sys.argv)
mainwindow = WindowClass()
mainwindow.show()
app.exec_()