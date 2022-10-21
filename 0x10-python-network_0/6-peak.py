#!/usr/bin/python3

"""
defines a function that finds a peak in a list of unsorted integers
"""
def find_peak(list_of_integers):
    """returns the peak element or 
    None if it doesn't exit"""
    if (list_of_integers):
        list_of_integers.sort()
        return (list_of_integers[-1])
