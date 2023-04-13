#!\usr\bin\python3
"""Contains the function that appends string"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.
    If the file doesn't exist, it will be created.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
