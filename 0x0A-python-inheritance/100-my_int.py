#!/usr/bin/python3
"""
This program creates a class MyInt
"""


class MyInt(int):
    """
    Class MyInt is a rebel.
    MyInt has == and != operations inverted
    """

    def __init__(self, other_num):
        """changes equal to to not equal to"""
        return

    def __ne__(self, other_num):
        """
        changes 'not equal to' to 'equal to'
        """
        return super().__eq__(other_num)

    def __eq__(self, other_num):
        """
        Changes 'equal to' to 'not equal to'
        """
        return super().__ne__(other_num)
