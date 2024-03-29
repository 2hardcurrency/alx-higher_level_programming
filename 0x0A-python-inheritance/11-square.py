#!/usr/bin/python3
"""Contains the square that inherites fron the rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return (self.__size) ** 2

    def __str__(self):
        """Reruens the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
