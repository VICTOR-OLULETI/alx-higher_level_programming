#!/usr/bin/python3
"""
This program reads files
"""


def read_file(filename=""):
    """
    This function reads the file and prints it out
    Args: filename - (.txt) file
    """
    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end="")
