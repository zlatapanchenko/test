from PyQt5 import QtCore
from instr import*
from screen3 import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connection()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.rv_line = QVBoxLayout()
        self.lv_line = QVBoxLayout()
        self.surname = QLabel(txt_name)
        self.age = QLabel(txt_age)
        self.start = QLabel(txt_test1)
        self.test2 = QLabel(txt_test2)
        self.test3 = QLabel(txt_test3)
        self.timer = QLabel()
        self.button1 = QPushButton(txt_starttest1)
        self.button2 = QPushButton(txt_starttest2)
        self.button3 = QPushButton(txt_starttest3)
        self.button4 = QPushButton(txt_sendresults)
        self.btn = QLineEdit(txt_hintname)
        self.btn2 = QLineEdit(txt_hintage)
        self.btn3 = QLineEdit(txt_hinttest1)
        self.btn4 = QLineEdit(txt_hinttest2)
        self.btn5 = QLineEdit(txt_hinttest3)
        self.lv_line.addWidget(self.surname, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.btn, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.btn2, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.start, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.button1, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.btn3, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.test2, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.button2, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.test3, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.button3, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.btn4, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.btn5, alignment = Qt.AlignLeft)
        self.lv_line.addWidget(self.button4, alignment = Qt.AlignCenter)
        self.rv_line.addWidget(self.timer, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.lv_line)
        self.h_line.addLayout(self.rv_line)
        self.setLayout(self.h_line)
    def connection(self):
        self.button4.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.string = string()
app = QApplication([])
window = TestWin()
app.exec_()