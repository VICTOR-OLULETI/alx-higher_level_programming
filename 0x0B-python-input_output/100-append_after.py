#!/usr/bin/python
"""
This program inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """This function opens and reads the file, searches the string
    and inserts the new_string at each line containing the search
    string
    Args:
        filename: string
        search_string: string
        new_string: string
    """
    with open(filename, encoding="utf+8", mode="r+") as myFile:
        readFile = myFile.readlines()
        newFile = ""

        for line in readFile:
            newFile += line
            if (search_string in line):
                newFile += new_string

        myFile.seek(0)
        myFile.write(newFile)
