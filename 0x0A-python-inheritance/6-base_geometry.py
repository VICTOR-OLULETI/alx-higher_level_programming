#!/usr/bin/python3
"""This program createa a class and raises and exception"""


class BaseGeometry:
    """
    This class raises an exception
    """

    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")
