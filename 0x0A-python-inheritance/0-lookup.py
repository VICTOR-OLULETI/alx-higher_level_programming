#!/usr/bin/python3
"""This program gets the list of available
    attributes and methods of an object
"""


def lookup(obj):
    """This function  returns a list of
    the attributes and methods of the object
    Args:
        obj: object
    """
    return (dir(obj))
