import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtCore

form_class = uic.loadUiType(r"C:\Users\crebi\Documents\GitHub\PyQt5\Designer\14_Notepad_RadioButton\notepad.ui")[0]

class FindWindow(QDialog):
    def __init__(self, parent):
        super(FindWindow, self).__init__(parent)
        uic.loadUi(r"C:\Users\crebi\Documents\GitHub\PyQt5\Designer\14_Notepad_RadioButton\find.ui", self)
        self.show()

        self.parent = parent
        self.cursor = parent.plainTextEdit.textCursor()
        self.pTE = parent.plainTextEdit
        
        self.pushButton_findnext.clicked.connect(self.findnext)
        self.pushButton_cancel.clicked.connect(self.close)

        self.radioButton_down.clicked.connect(self.updown_radio_button)
        self.radioButton_up.clicked.connect(self.updown_radio_button)
    
    def updown_radio_button(self):
        if self.radioButton_down.isChecked():
            print("down")
        elif self.radioButton_up.isChecked():
            print("up")
    
    def keyReleaseEvent(self, event):
        # print(self.lineEdit.text())
        if self.lineEdit.text():
            self.pushButton_findnext.setEnabled(True)
        else:
            self.pushButton_findnext.setEnabled(False)

    def findnext(self):
        pattern = self.lineEdit.text()
        text = self.pTE.toPlainText()
        
        reg = QtCore.QRegExp(pattern)
        index = reg.indexIn(text, 0)
        if index != -1:
            self.setCursor(index, len(pattern)+index)

    def setCursor(self, start, end):
        print(self.cursor.selectionStart(), self.cursor.selectionEnd())
        self.cursor.setPosition(start)
        self.cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, end-start)
        self.pTE.setTextCursor(self.cursor)                

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

        self.action_find.triggered.connect(self.findFunction)

        self.opened = False
        self.opened_filepath = '제목 없음'

    def isChanged(self):
        if not self.opened:
            if self.plainTextEdit.toPlainText().strip():
                return True
            return False
        current_data = self.plainTextEdit.toPlainText()
        with open(self.opened_filepath, encoding = 'UTF8') as f:
            file_data = f.read()

        if current_data == file_data: return False
        else: return True

    def save_changed_data(self):
        msgBox = QMessageBox()
        msgBox.setText("변경내용을 {}에 저장하시겠습니까?".format(self.opened_filepath))
        msgBox.addButton("저장", QMessageBox.YesRole)
        msgBox.addButton("저장 안 함", QMessageBox.NoRole)
        msgBox.addButton("취소", QMessageBox.RejectRole)
        ret = msgBox.exec_()
        if ret == 0: self.saveFunction()
        else: return ret
        
    def closeEvent(self, event):
        if self.isChanged():
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
        if self.isChanged():
            ret = self.save_changed_data()
            
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

    def findFunction(self):
        FindWindow(self)

app = QApplication(sys.argv)
mainwindow = WindowClass()
mainwindow.show()
app.exec_()