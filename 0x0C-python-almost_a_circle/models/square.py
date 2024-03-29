#!/usr/bin/python3
"""Contains class of square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square"""
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        self.width = value

    @size.setter
    def size(self, value):
        """Get/set the size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for keys, values in kwargs.items():
                if keys == "id":
                    if values = None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif keys == "size":
                    self.size = value
                elif keys == "x":
                    self.x = value
                elif keys == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return ("id": self.id, "size": self.width, "x": self.x, "y": self.y)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.width, self.x,
                                                 self.y)
