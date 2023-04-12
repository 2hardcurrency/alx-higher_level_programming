#!/usr/bin/python3


BaseGeometry = __import__(8-rectangle.py).BaseGeometry


def area(self):
    """Defines the area of the Rectangle"""
    return (self._width) * (self._height)

def __str__(self):
    """informal string representation of the rectangle"""
    return "[Rectangle]{:d}/{:d}", (self._width, self._height)
