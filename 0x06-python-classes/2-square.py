#!/usr/bin/python3

""" class of square definition"""

class Square:

    """ square with a private instance attribute"""
    def __init__ (self, size = 0):

        """
        Args:
        size: size of square
        """
        if (type(size is int)):

            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size**2

        else:
            raise TypeError("size must be an integer")
        
