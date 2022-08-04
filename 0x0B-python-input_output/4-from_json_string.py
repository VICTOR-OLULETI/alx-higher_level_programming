#!/usr/bin/python3
"""
This program converts JSON to
Python data structure
"""


import json


def from_json_string(my_str):
    """
    returns an Object(Python data structure)
    Args:
        my_str: string
    """
    return (json.loads(my_str))
