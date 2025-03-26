import os
def save_to_file(content: str, filename: str):
    """Save content to a file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(content)
