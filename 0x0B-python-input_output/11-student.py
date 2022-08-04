#!/usr/bin/python3
"""
This program defines a Student
"""


class Student:
    """This class defines a Student based on
        first_name, last_name and age
    """
    def __init__(self, first_name, last_name, age):
        """Constructor for the student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            value = self.__dict__.get(attr)
            if value is not None:
                result[attr] = value

        return result

    def reload_from_json(self, json):
        """
        Update all public instance attributes
        Args:
            json: dict
        """
        for key, value in json.items():
            if (self.__dict__.get(key) == self.first_name):
                self.first_name = value
            elif (self.__dict__.get(key) == self.last_name):
                self.last_name = value
            elif (self.__dict__.get(key) == self.age):
                self.age = value
