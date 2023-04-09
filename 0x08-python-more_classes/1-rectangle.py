#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width for private instance"""
        return self.__width

    @height.setters
    def width(self, value):
        """Sets the width for private instance"""

        if type(width) is int:
            if width < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """Getter for the private instance attribute"""
        return self.__height

    @height.setters
    def height(self, value):
        """Setter for the private instance attribute"""
        if type(height) not int:
            if height < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = value
        else:
            raise TypeError('height must be an integer')
