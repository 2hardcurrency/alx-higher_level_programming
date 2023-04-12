#!/usr/bin/python3
"""Contains an empty class"""


class BaseGeometry:
    """Defines an empty class, BaseGeometry"""
    def area(self):
        """Defines the class that raises exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""

        if type(value) is not int:
            raise TypeError('{:s} must be an integer')
        if value <= 0:
            raise ValueError('{:s} must be greater than 0')
