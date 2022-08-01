#!/usr/bin/python3
"""This program raises an exception and integer
    validation
"""


class BaseGeometry:
    """
    creates the area and integer_validator
    methods
    """

    def area(self):
        """
        raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        raises an exception if error is found
        Args:
            name: string
            value: integer
        """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))

        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
