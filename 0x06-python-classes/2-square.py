#!/usr/bin/python3
"""Class Square with size validation """


class Square:
    """Class Square with size validation"""

    def __init__(self, size=0):
        """Constructor of a Square with size"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size
