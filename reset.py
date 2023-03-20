import shutil

reset_choice = input("Are you sure you want to reset Clown Browser? (y/n): ")

if reset_choice == "y":
    print("Resetting Clown Browser...")
    shutil.rmtree(webcache_folder)
    print("Deleting Website Cache...")
    print("Deleting Python Cache...")
    shutil.rmtree("__pycache__")
elif reset_choice == "n":
    print("Reset Cancelled: User Choice")
else:
    print("Reset Cancelled: Invalid Option")
