#!/usr/bin/python3
"""
Contains a class of rectangle that inherits base
"""


class Rectangle(Base):
    """Represent a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
         """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    super().__init__id

    @property
    def width(self):
        """getter for the attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the attributes"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the attributes"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """getter for the attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the attributes"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for the attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the attributes"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Defines the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or if self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

