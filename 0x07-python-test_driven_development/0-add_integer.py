#!/usr/bin/python3
"""My Addition calculation module"""


def add_integer(a, b=98):
    """
    Addition Function
    Args
        a: int or float
        b: int or float
    """

    if (type(a) not in [int, float]):
        raise TypeError("a must be an integer")
    elif (type(b) not in [int, float]):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
