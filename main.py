from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


def show_message(message):
    
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Hello world!'))
layout.addWidget(QPushButton('Hello world! 2'))
window.setLayout(layout)
window.show()
app.exec_()