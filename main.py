# Import from other files
from puppets.reset import reset_app
from comedious.comedy import MainWindow
# Import required Qt and other stuff
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(554, 306)
    widget.show()

    sys.exit(app.exec())
    