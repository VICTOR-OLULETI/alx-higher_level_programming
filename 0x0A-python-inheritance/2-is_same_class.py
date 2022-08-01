#!/usr/bin/python3
"""This program checks if object is an
    instance of the specified class
    Args:
        obj: object
        a_class: class
"""


def is_same_class(obj, a_class):
    """Returns true if the object is exactly
        an instance of the specified class else
        false
    """
    return type(obj) == a_class
