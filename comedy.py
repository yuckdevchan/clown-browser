import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.icon_pixmap = QPixmap("icon.ico")
        self.app_icon = QIcon(self.icon_pixmap)
        self.setWindowIcon(self.app_icon)

        # self.text = QtWidgets.QLabel("Type a URL:", alignment=QtCore.Qt.AlignTop)
        self.url_input_box = QtWidgets.QLineEdit(self)
        self.url_input_box.setPlaceholderText("Enter a URL...")
        self.open_button = QtWidgets.QPushButton("Open")
        self.quit_button = QtWidgets.QPushButton("Quit")

        self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.text)
        self.layout.addWidget(self.open_button)
        self.layout.addWidget(self.quit_button)

        self.setWindowTitle("Clown Browser - Comedious Frontend")

        self.open_button.clicked.connect(self.download)
        self.quit_button.clicked.connect(self.quit)

    @QtCore.Slot()
    def download(self):
        print("Opening Webpage...")
    def quit(self):
        pass


