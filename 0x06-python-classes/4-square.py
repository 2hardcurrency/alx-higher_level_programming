#!/usr/bin/python3
"""defines a square"""
class Square:
    """Represents the square
    Attributes:
        __size (int): size of a side of the square
        """
    def __init__(self, size=0):
        """Initializes the square."""

        self.size = size

    def area(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size"""


        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')
