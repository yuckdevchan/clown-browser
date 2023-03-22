# Import from other files
from puppets.reset import reset_app
from puppets.marionette import cli_args
from comedious.comedy import MainWindow
from comedious.funny import app_version
# Import required Qt and other stuff
import sys, argparse, colorama
from colorama import Fore
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

cli_args(program_name=f"Clown Browser {app_version}", program_desc="A Web Browser for Clowns")

print(Fore.MAGENTA + f"Clown Browser {app_version}\n" + Fore.WHITE)

# argparse stuff
parser = argparse.ArgumentParser(
    prog="Clown Browser",
    description="Web Browser for Clowns.")
arg_group = parser.add_mutually_exclusive_group()
arg_group.add_argument('-r', '--reset', action="store_true", help="Reset Clown Browser")
print(parser.parse_args())
args = parser.parse_args()

if args.reset:
    reset_app()
else:
    print("Launching Comedious...")

# Run the program
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(554, 306)
    widget.show()

    sys.exit(app.exec())
