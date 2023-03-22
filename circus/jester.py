# Circus Web Engine (ɔ) 2023
import os
from bs4 import BeautifulSoup
from circus.joker import html_render_fail, empty_file_check

def validation(html_file):
    empty_file_check(html_file)

def render_html(html_file):
    print("Circus[Jester]: Recieved HTML file")
    validation(html_file)
    print("Circus[Jester]: Rendering HTML...")
    soup_html_parser = BeautifulSoup(html, 'html.parser')
    website_element_title = soup_html_parser.find('title')
    print(f"Circus[Jester]: HTML title: {website_element_title}")
