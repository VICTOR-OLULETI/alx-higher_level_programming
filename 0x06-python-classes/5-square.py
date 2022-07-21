#!/usr/bin/python3
"""Class Square """


class Square:
    """Class Square with size"""
    def __init__(self, size=0):
        """Class construct"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method to get the area of the Square"""
        return (self.__size ** 2)

    def my_print(self):
        """Method to print Square"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    @property
    def size(self):
        """Getter of the private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the private attribute size"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value
