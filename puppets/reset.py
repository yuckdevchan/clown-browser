# Import shutil to delete folders (because 'os' is bad)
import shutil, os
# Import random other stuff
from comedious.funny import webcache_folder

def reset_app():
    reset_choice = input("Are you sure you want to reset Clown Browser? (y, n) ")

    if reset_choice == "y":
        print("Resetting Clown Browser...")
        if os.path.isdir(webcache_folder) == False:
            print("There is not web cache.")
        else:
            print("Deleting Website Cache...")
            shutil.rmtree(webcache_folder)
        if os.path.isdir("__pycache__") == False:
            print("There is not python cache in root.")
        else:
            print("Deleting Python Cache in root...")
            shutil.rmtree("__pycache__")
    elif reset_choice == "n":
        print("Reset Cancelled: User Choice")
    else:
        print("Reset Cancelled: Invalid Option")
