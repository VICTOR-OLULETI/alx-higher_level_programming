#!/usr/bin/python3
"""
Class Magic Class:
-area function
-circumference function
"""
import math


class MagicClass:
    """Class MagicClass with area and circumference """
    def __init__(self, radius=0):
        """Construct of MagicClass"""
        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """get area"""
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        """get circumference"""
        return (2 * math.pi * self.__radius)
