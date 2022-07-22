#!/usr/bin/python3
"""
Class Square defined by
-size(private instance)
-area(public instance)
"""


class Square:
    """Class Square with size and area"""
    def __init__(self, size=0):
        """Construct for Class Square"""
        if (type(size) is not int) and (type(size) is not float):
            raise TypeError("size must be a number")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)

    def __eq__(self, other):
        """Compare operator '==' """
        return (self.area() == other.area())

    def __ne__(self, other):
        """Compare operator '!=' """
        return (self.area() != other.area())

    def __gt__(self, other):
        """Compare operator '>' """
        return (self.area() > other.area())

    def __ge__(self, other):
        """Compare operator '>=' """
        return (self.area() >= other.area())

    def __lt__(self, other):
        """Compare operator '<' """
        return (self.area() < other.area())

    def __le__(self, other):
        """Compare operator '<=' """
        return (self.area() <= other.area())

    @property
    def size(self):
        """Getter for private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for private attribute size"""
        if (type(size) is not int) and (type(size) is not float):
            raise TypeError("size must be a number")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
