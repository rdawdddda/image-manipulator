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
from manipylator_dll import *
    
styles_for_btn = """
    QPushButton {
        height: 40px;
        width: 100px; 
        color: white;
        border-style: outset;
        border-width: 1px;
        border-radius: 5px;
        border-color: white;
        padding: 10px;
        font-weight: 600;
        background: MintCream;
    }
    QPushButton:hover {
        color: gray;
        border: 1px solid gray;
        font-weight: 700;
    }
    QPushButton::active {
        color: blue;
        border-color: gray;
        font-size: 10px
    }
    """

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

layout_v = QVBoxLayout()
layout_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()
layout_v.addLayout(layout_h1)
layout_v.addLayout(layout_h2)
layout.addLayout(layout_v)

btn_info = QPushButton("Информация\no изображении")
btn_info.setStyleSheet(styles_for_btn)
layout_h1.addWidget(btn_info)

btn_MBW = QPushButton("Сделать \n черно-белым")
btn_MBW.setStyleSheet(styles_for_btn)
btn_MBW.clicked.connect(
    lambda: MBW(input_image)
)
layout_h1.addWidget(btn_MBW)

btn_pencil = QPushButton("Карандашом")
btn_pencil.setStyleSheet(styles_for_btn)
btn_pencil.clicked.connect(
    lambda: contour(input_image)
)
layout_h1.addWidget(btn_pencil)

btn_emboss = QPushButton("тиснение")
btn_emboss.setStyleSheet(styles_for_btn)
btn_emboss.clicked.connect(
    lambda: emboss(input_image)
)
layout_h2.addWidget(btn_emboss)

btn_flip = QPushButton("отзеркаливание")
btn_flip.setStyleSheet(styles_for_btn)
btn_flip.clicked.connect(
    lambda: flip(input_image)
)
layout_h2.addWidget(btn_flip)

btn_rotate = QPushButton("разворот")
btn_rotate.setStyleSheet(styles_for_btn)
btn_rotate.clicked.connect(
    lambda: blur(input_image)
)
layout_h2.addWidget(btn_rotate)

window.setLayout(layout)
window.resize(350, 0)
window.show()
app.exec_()

