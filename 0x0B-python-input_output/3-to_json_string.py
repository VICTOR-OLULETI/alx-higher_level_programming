#!/usr/bin/python3
"""
This program converts object to JSON
"""


import json


def to_json_string(my_obj):
    """
    Converts 'my_obj' to JSON representation
    Args:
        my_obj : dictionary
    """
    return (json.dumps(my_obj))
