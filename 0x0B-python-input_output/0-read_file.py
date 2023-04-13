#!/usr/bin/python3
"""opening a file for read-only"""


def read_file(filename=""):
    """Defining the file operations"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
