#!/usr/bin/python3
"""
This program adds a new attribute to an object
"""


def add_attribute(obj, key, value):
    """
    This function tries to add a new attribute
    or raises an error if not
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, key, value)
