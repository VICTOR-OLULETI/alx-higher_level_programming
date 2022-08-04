#!/usr/bin/python3
"""
This program defines a Student in a Class
"""


class Student():
    """
    Class of a Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructor of a student
        Args:
            - first_name: string
            - last_name : string
            - age: integer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return the dict representation
        """
        return (self.__dict__)
