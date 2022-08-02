#!/usr/bin/python3
"""
This program defines a Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class square inherits from Rectangle
    Args:
        size: positive integer
    """
    def __init__(self, size):
        """
        Constructor for the Square class
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)
