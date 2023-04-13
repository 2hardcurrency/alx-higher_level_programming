#!/usr/bin/python3
"""Contains the write-only file"""


def write_file(filename="", text=""):
    """Writes into a file in stdout"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
