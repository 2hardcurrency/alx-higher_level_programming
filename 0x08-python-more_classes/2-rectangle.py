#!/usr/bin/python3
"""
Defines a class rectangle
"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width for private instance"""
        return self.__width

    @width.setters
    def width(self, value):
        """Sets the width for private instance"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance attribute"""
        return self.__height

    @height.setters
    def height(self, value):
        """Setter for the private instance attribute"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Defines the area of a rectangle
        Returns:
            area of rectangle
            """
        return (self.__width) * (self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (self.__height * 2)
