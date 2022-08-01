#!/usr/bin/python3
"""This program prints a list sorted
    using a class that inherits a list
    attribute
"""


class MyList(list):
    """This class Mylist inherits
        from the list
    """

    def print_sorted(self):
        print(sorted(self))
