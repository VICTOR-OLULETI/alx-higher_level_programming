#!/usr/bin/python3
"""My Rectangle Class"""


class Rectangle:
    """Rectangle class with width and height"""
    def __init__(self, width=0, height=0):
        """Constructor of class Rectangle
                Args:
                    - width (default = 0): int
                    - height (default = 0): int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for private instance width
                Args:
                    - value: int
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance height
                Args:
                    - value: int
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
