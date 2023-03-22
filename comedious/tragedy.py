# Tragedy: Functions and bits used by comedy
# Import QT and other stuff
import time, os, urllib3, wget
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from colorama import Fore
from bs4 import BeautifulSoup
# Import stuff from other files
from comedious.funny import clown_folder, webcache_folder, quit_app
from circus.jester import render_html
from puppets.marionette import args_quiet, args_verbose

def create_website_path(url_input):
    path = os.path.join(clown_folder, webcache_folder, url_input.split("//")[1])
    if os.path.isdir(path) == False:
        print(f"Creating website path: {path}.")
        os.makedirs(path)
    else:
        pass
    
def download_stylesheets():
    soup = BeautifulSoup(response.content, 'html.parser')
    stylesheet_links = soup.head.find_all('link', rel='stylesheet')

def download_html_index(main_window, url_input):
    print("Comedious[Tragedy]: Downloading index.html...")
    main_window.status_text.setText("Downloading index.html...")
    index_load_time = time.process_time()
    website_index = url_input + "/index.html"
    # Call create_website_path Function
    create_website_path(url_input)
    # Download Website
    path = os.path.join(clown_folder, webcache_folder, url_input.split("//")[1])
    start = time.process_time()
    index_file = wget.download(website_index, out=path)
    # Website download is a success (probably)
    website_download_success_text = Fore.GREEN + f"\nComedious[Tragedy]: Downloaded 'index.html' from {url_input} in {str(time.process_time() - start)} seconds." + Fore.WHITE
    website_download_success_text_gui = f"\nDownloaded 'index.html' from {url_input} in {str(time.process_time() - start)} seconds."
    print(website_download_success_text)
    main_window.status_text.setText(website_download_success_text_gui)
    # Call render html function
    index_html_file_path = os.path.join(path, "index.html")
    print("Comedious[Tragedy]: Sending HTML file to Joker...")
    render_html(html_file="index_html_file_path")
    
def user_search(main_window):
    url_input = main_window.url_input_box.text()
    print("URL Entered:", url_input)
    # Check what kind of connection it is (http or https)
    if url_input.startswith("https://") == True:
        url_input_valid = True
        print(Fore.GREEN + "\nComedious[Tragedy]: Passed Check #1: Is a valid URL, of type: " + Fore.BLUE + "HTTPS (Hypertext Transfer Protocol Secure)" + Fore.WHITE)
    elif url_input.startswith("http://") == True:
        url_input_valid = True
        print(Fore.GREEN + "Comedious[Tragedy]: Passed Check #1: Is a valid URL, of type: " + Fore.RED + "HTTP (Hypertext Transfer Protocol (INSECURE - Unencrypted Connection.))" + Fore.WHITE)
    else:
        url_input_valid = False
        print("\nComedious[Tragedy]: Failed Check #1: Is not a valid URL, of type HTTPS or HTTPS")
        print("\nComedious[Tragedy]: Exiting")
        for i in range(3, 0, -1):
            time.sleep(1)
            print(i)
            quit_app()
    if url_input_valid:
        main_window.status_text.setText("URL is Valid, Connecting to Website")
        start = time.process_time()
        http = urllib3.PoolManager()
        http_code = http.request('GET', url_input)
        if str(http_code.status) == "200":
            print(Fore.GREEN + "Website returned code: " + str(http_code.status) + Fore.WHITE)
            print(f"Succesfully conected to: {url_input}.")
            main_window.status_text.setText(Fore.GREEN + f"Successful connected to: {url_input}." + Fore.WHITE)
            # Call download index.html
            download_html_index(main_window, url_input)
        else:
            print("Website returned code: " + str(http_code.status))
            main_window.status_text.setText(Fore.RED + f"Could not connect to: {url_input}." + Fore.WHITE)

def set_app_icon(main_window, icon_variable):
    main_window.icon_pixmap = QPixmap(icon_variable)
    main_window.app_icon = QIcon(main_window.icon_pixmap)
    main_window.setWindowIcon(main_window.app_icon)
