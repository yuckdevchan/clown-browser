# Circus Web Engine (ɔ) 2023
import os
from colorama import Fore
from urllib.request import urlopen
from bs4 import BeautifulSoup
from circus.joker import html_render_fail, empty_file_check

# def validation(html_file):
#     empty_file_check(html_file)

def render_html(html_file):
    print("Circus[Jester]: " + Fore.BLUE + "Recieved HTML file" + Fore.WHITE)
    # validation(html_file)
    print("Circus[Jester]: " + Fore.BLUE + "Rendering HTML..." + Fore.WHITE)
    with open(html_file, "r") as f:
        file_contents = "".join(f.readlines()) 
    soup_url = BeautifulSoup(file_contents, "html.parser")
    website_element_title = soup_url.find("title").get_text()
    print(f"Circus[Jester]: " + Fore.BLUE + "HTML title: " + Fore.MAGENTA + website_element_title + Fore.WHITE)
    