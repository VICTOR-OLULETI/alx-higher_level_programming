#!/usr/bin/python3
"""Class Square with area"""


class Square:
    """Square with area"""
    def __init__(self, size=0):
        """Constructor Square"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """Square area"""
        return (self.__size ** 2)
