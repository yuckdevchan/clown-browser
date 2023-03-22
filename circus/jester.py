# Circus Web Engine (ɔ) 2023
import os
from bs4 import BeautifulSoup
from circus.joker import html_render_fail, empty_file_check

def validation(html_file):
    empty_file_check()

def render_html(html_file):
    validation()
    print("Circus[Jester]: Rendering HTML...")