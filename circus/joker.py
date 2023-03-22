def html_render_fail(error_reason):
    print(f"Circus[Joker]: Failed to render HTML!\nError: {error_reason}")

def empty_file_check(html_file):
    if os.stat(html_file).st_size == 0:
        html_render_fail("HTML File is Empty!")
