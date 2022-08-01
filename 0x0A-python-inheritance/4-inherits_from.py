#!/usr/bin/python3
"""
    Checks if a class inherit from a class
    directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    else False
    """
    if type(obj) == a_class:
        return (False)
    return isinstance(obj, a_class)
