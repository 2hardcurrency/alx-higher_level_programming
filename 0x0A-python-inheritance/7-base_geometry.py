#!/usr/bin/python3
"""Contains an empty class"""


class BaseGeometry:
    """Defines an empty class, BaseGeometry"""
    def area(self):
        """Defines the class that raises exception"""
        raise exception('area() is not implemented')

    def integer_validator(self, name, value):

        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError('{:s} must be an integer')
        if value <= 0:
            raise ValueError('{:s} must be greater than 0')
