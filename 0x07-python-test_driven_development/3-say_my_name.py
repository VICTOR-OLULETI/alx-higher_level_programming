#!/usr/bin/python3
""" My name module """


def say_my_name(first_name, last_name=""):
    """ Returns the users first_name and last_name if provided"""

    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")

    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")

    name = "My name is {} {}".format(first_name, last_name)
    print(name)
