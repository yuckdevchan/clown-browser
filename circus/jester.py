# Circus Web Engine (ɔ) 2023
import os
from circus.joker import html_render_fail

def validation(html_file):

def render_html(html_file):
    print("Circus[Jester]: Rendering HTML...")
    if os.stat(html_file).st_size == 0:
        fail("HTML File is Empty!")
