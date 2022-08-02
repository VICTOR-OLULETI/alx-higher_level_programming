#!/usr/bin/python3
"""This program creates a class and demonstrates
    inheritance
"""


PrevSquare = __import__('10-square').Square


class Square(PrevSquare):
    """Class Square with
        Args:
            size: positive integer
    """
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size)
