#!/usr/bin/python3
"""
Contains the function that adds to integers
"""


def add_integer(a, b=98):
    if a is not int and a is not float:
        raise TypeError("a must be an integer")
    if b is not int and b is not float:
        raise TypeError("b must be an integer")
    if a is float:
        a = int(a)
    if b is float:
        b = int(b)


return a + b
