#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    keys = list(new)

    for i in keys:
        new[i] *= 2
    return new
