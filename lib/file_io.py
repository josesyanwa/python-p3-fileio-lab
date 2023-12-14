def write_file(file_name, file_content):
    """Write file_content to a .txt file."""
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """Append append_content to a .txt file."""
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)

def read_file(file_name):
    """Read and return the content of a .txt file."""
    with open(f'{file_name}.txt', 'r') as f:
        file_content = f.read()
    return file_content
