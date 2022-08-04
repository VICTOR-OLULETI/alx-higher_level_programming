#!/usr/bin/python3
"""
This program appends text into a file
and creates the file if it doesn't exist
"""


def append_write(filename="", text=""):
    """
    This function appends to the file and
    returns the number of character added
    """
    with open(filename, encoding="utf-8", mode="a") as myFile:
        value = myFile.write(text)

    return (value)
