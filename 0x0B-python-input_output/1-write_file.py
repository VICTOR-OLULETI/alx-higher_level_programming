#!/usr/bin/python3
"""
This program writes a string in a text file
"""


def write_file(filename="", text=""):
    """This function writes into a file and
    returns the number of characters written
    """
    with open(filename, encoding="utf-8", mode='w') as myFile:
        value = myFile.write(text)

    return (value)
