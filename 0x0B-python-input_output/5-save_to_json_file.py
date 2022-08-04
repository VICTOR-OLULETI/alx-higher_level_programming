#!/usr/bin/python3
"""
This program writes an object to a text file,
using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This function Saves Object file in
    JSON format.
    Args:
        my_obj
        filename: string
    """
    with open(filename, encoding="utf-8", mode="w") as myFile:
        myFile.write(json.dumps(my_obj))
