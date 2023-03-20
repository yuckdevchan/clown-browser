# Circus Web Engine (ɔ) 2023
import os

def fail(error_reason):
    print(f"Failed to render HTML!\nError Code: {error_reason}")

def render_html(html_file):
    print("Circus: Rendering HTML...")
    if os.stat(html_file).st_size == 0:
        fail("HTML File is Empty!")
        