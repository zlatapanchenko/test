from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import*
from screen2 import*

class MainWin(QWidget):
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
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.button,alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
    def connection(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.Object = Objects()
app = QApplication([])
window = MainWin()
app.exec_()