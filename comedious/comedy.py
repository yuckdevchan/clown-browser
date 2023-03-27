# Comedy: The GUI front-end for Clown Browser
# Import required Qt and other stuff
import sys, random, urllib3.request, time, os, wget, colorama
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from colorama import Fore
# Import tragic stuff
from comedious.tragedy import download_html_index, user_search, set_app_icon
from comedious.funny import app_version, quit_app

print(Fore.BLUE + "Launching Comedy..." + Fore.WHITE)

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # App Icon
        set_app_icon(self, icon_variable="logo.ico")

        # self.text = QtWidgets.QLabel("Type a URL:", alignment=QtCore.Qt.AlignTop)

        # URL Input Text Box
        self.url_input_box = QtWidgets.QLineEdit(self)
        self.url_input_box.setPlaceholderText("Enter a URL...")
        self.url_input_box.returnPressed.connect(self.user_search)
        
        # Menu Buttons
        self.open_button = QtWidgets.QPushButton("Open this URL")
        self.reset_button = QtWidgets.QPushButton("Reset Clown Browser")
        self.quit_button = QtWidgets.QPushButton("Quit App")

        # Status
        self.status_text = QtWidgets.QLabel("Awaiting Input...")

        # Layout Stuff
        self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.text)
        self.layout.addWidget(self.status_text)
        self.layout.addWidget(self.open_button)
        self.layout.addWidget(self.reset_button)
        self.layout.addWidget(self.quit_button)

        self.setWindowTitle(f"Clown Browser {app_version} - Comedious Frontend")

        # Connect Actions
        self.open_button.clicked.connect(self.user_search)
        self.reset_button.clicked.connect(self.pass_this) # Reset button runs reset function from reset.py
        self.quit_button.clicked.connect(quit_app)

    def user_search(self):
        user_search(self)

    @QtCore.Slot()
    # Action Functions
    def pass_this(self):
        pass