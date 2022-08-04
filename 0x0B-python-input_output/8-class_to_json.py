#!/usr/bin/python3
"""
This program returns the dict representation
of a instance of Class.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data
    Args:
        -ob: instance of class
    """

    return (obj.__dict__)
