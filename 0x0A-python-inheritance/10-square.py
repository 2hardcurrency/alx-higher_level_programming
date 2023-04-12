#!/usr/bin/python3
"""Contains the square that inherites fron the rectangle"""


class Square(Rectangle):
    """Defines the class of square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return (self.__size) ** 2
