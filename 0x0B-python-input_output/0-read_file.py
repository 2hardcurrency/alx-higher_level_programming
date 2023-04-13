#!/usr/bin/python3
"""opening a file for read-only"""


def read_file(filename=""):
    """Defining the file operations"""
    with open('workfile', encoding="utf-8") as f:
        """opening a file for read-only"""
        print(f.read(), end='')
