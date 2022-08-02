#!/usr/bin/python3
"""This program inherits a class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle:
        Args:
            width: positive int
            height: positive int
    """
    def __init__(self, width, height):
        """Constructor for width and height"""
        BaseGeometry.integer_validator(self, "", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "", height)
        self.__height = height
