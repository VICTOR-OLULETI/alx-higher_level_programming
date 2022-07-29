#!/usr/bin/python3
"""This program prevents the user from dynamically
    creating new instance attributes
"""


class LockedClass:
    """Only first_name instance can be created by user"""
    __slots__ = ['first_name']
