#!/usr/bin/python3
"""This program checks if the object is an instance of a class,
    that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance of,
    or instance of a class inherited from the specified
    class
    """
    return (isinstance(obj, a_class))
