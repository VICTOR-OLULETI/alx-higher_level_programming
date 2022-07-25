#!/usr/bin/python3
"""My Sqaure module"""


def print_square(size):
    """Prints a Square based on size given"""

    if (type(size) is not int):
        raise TypeError("size must be an integer")

    if (size < 0):
        raise ValueError("size must be >= 0")

    if (type(size) is float and size <= 0):
        raise TypeError("size must be an integer")
    if size != 0:
        for i in range(size):
            print('#' * size)
