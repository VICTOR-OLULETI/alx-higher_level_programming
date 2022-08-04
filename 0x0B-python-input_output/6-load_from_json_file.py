#!/usr/bin/python3
"""
This program creates object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    This function createa an Object from a
    JSON file
    Args:
        filename: JSON file
    """
    with open(filename, encoding="utf-8", mode="r") as myFile:
        return json.loads(myFile.read())
