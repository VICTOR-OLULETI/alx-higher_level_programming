#!/usr/bin/python3
"""
This program takes a text and inserts 2 new lines after each delimiter
('.', '?', ':')
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these charaters:
        '.?:'
        Args:
            - text (type string)
    """
    if (type(text) is not str):
        raise TypeError("text must be a string")

    indentation = '.?:'
    text_edit = text

    for ch in indentation:
        text_edit = f'{ch}\n\n'.join(
                list(map(lambda w: w.strip(' '), text_edit.split(ch)))
                )
    print(text_edit, end='')
