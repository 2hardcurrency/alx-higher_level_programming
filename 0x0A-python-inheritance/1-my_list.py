#!/usr/bin/python3
"""Contains the MyList class"""


class MyList(List):
    """A sorted class list"""

    def __init__(self):
        """Defines the function"""
        super().__init__()

    def print_sorted(self):
        """That prints the sorted list"""
        print(sorted(self))
