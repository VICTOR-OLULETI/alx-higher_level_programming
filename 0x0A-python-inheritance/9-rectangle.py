#!/usr/bin/python3
"""
This program creates a class and demonstrates
inheritance
"""


BaseGeometry = __import__('8-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherits the BaseGeometry
        Args:
            width: integer
            height: integer
    """
    def __init__(self, width, height):
        """
        Constructor of an instance of class Rectangle
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """
        area of the rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns string representation of class Rectangle
        """
        value = "[{}] {:d}/{:d}".format(type(self).__name__,
                self.__width, self.__height)
        return value
