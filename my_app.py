from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from instr import*
from PyQt5.QtWidgets import(
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout,
    QGridLayout,QGroupBox, QRadiobutton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from second_win import* 

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
       self.btn_next = QPushButton(txt_next)
       self.hello_text = QLabel(txt_hello)
       self.instruction = QLabel(txt_instruction)

       self.layout = QVBoxLayout()
       self.layout.addWidget(self.hello_text,alignment = Qt.AlignLeft)
       self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)
       self.setLayout(self.layout)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
def main():
    app = QApplication([])
    mw = MainWin()
    app.exec_()
    
main()
