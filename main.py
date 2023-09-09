# Clown Browser
# Import from other files
from puppets.reset import reset_app
from puppets.marionette import cli_args
from comedious.comedy import MainWindow
from comedious.funny import app_version
# Import required Qt and other stuff
import sys, colorama
from colorama import Fore
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

cli_args(program_name=f"Clown Browser {app_version}", program_desc="A Web Browser for Clowns")

print(Fore.MAGENTA + f"Clown Browser {app_version}\n" + Fore.WHITE)

# Run the program
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(554, 306)
    widget.show()

    sys.exit(app.exec())
