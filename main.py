from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget, 
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLineEdit,
    QLabel)
from PyQt5 import QtGui
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import pywinstyles

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

window.setWindowIcon(QtGui.QIcon('frame.png'))

pywinstyles.apply_style(window, "dark")

window.setStyleSheet("background:black;")
window.setWindowTitle("Манипулятор изображений")

input_image = QLineEdit()
input_image.setStyleSheet("color:white;border:1px solid gray;padding: 5px;")
input_image.setPlaceholderText("Введите названия изображения")
layout.addWidget(input_image)

window.setLayout(layout)
window.show()
app.exec_()
