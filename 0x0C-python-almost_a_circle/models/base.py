#!/usr/bin/python3
"""
This program defines the Base Class
"""

import json
import os
import csv
import turtle


class Base:
    """
    This defines the base class for
    other classes
    """
    # Private Class  Attribute
    __nb_objects = 0

    # Constructor
    def __init__(self, id=None):
        """
        Constructor of Base Class
        Args:
            id: int
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        This function returns the list of the JSON string
        representation.
        Args:
            - json_string: JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    @staticmethod
    def draw(list_rectangles,  list_squares):
        """
        Opens a window and draws all the Rectangles and Squares
        Args:
            - list_rectangles: list of rectangle instances
            - list_squares: list of square instances
        """
        turtle.color('blue')
        turtle.speed(1)

        if all(inst.__class__.__name__ == 'Rectangle'
                for inst in list_rectangles):
            for rect in list_rectangles:
                turtle.goto(rect.x, rect.y)
                for i in range(2):
                    turtle.pendown()
                    turtle.fd(rect.width)
                    turtle.rt(90)
                    turtle.fd(rect.height)
                    turtle.rt(90)
                    turtle.penup()
        if all(inst.__class__.__name__ == 'Square'
                for inst in list_squares):
            for sq in list_squares:
                turtle.goto(sq.x, sq.y)
                for i in range(4):
                    turtle.pendown()
                    turtle.fd(sq.size)
                    turtle.rt(90)
                    turtle.penup()
        turtle.done()

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON representation of list_objs to a file
        Args:
            - cls: class method
            - list_objs : list of Rectangle or Square instances
        """
        options  = ['Rectangle', 'Square']
        result = []
        name = ""

        if (list_objs is not None and len(list_objs)):
            name = type(list_objs[0]).__name__
            if (name in options):
                if all((type(obj).__name__ == name) for obj in list_objs):
                    result = [obj.to_dictionary() for obj in list_objs]
        value = cls.to_json_string(result)
        filename = (cls).__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as myFile:
            myFile.write(value)

    @classmethod
    def create(cls, **dictionary):
        """
        This function Returns an instance with all attributes already set
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        result = []
        filename = cls.__name__ + ".json"
        if not os.path.exists("./{:s}".format(filename)):
            return result
        with open(filename, mode="r", encoding="utf-8") as myFile:
            content_in = myFile.read()
        content_out = cls.from_json_string(content_in)
        for i in content_out:
            result.append(cls.create(**i))

        return result

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of objs into a csv file"""
        samples = ['Rectangle', 'Square']
        result = []
        compare = ""
        if (list_objs is not None and len(list_objs)):
            compare = type(list_objs[0]).__name__
            if compare in samples:
                if (all(type(obj).__name == compare) for obj in list_objs):
                    result = [obj.to_dictionary() for obj in list_objs]

        filename = (cls).__name__ + ".csv"
        # field names
        rectangle_field = ["id", "width", "height", "x", "y"]
        square_field = ["id", "size", "x", "y"]

        with open(filename, mode="w", encoding="utf-8") as csvFile:
            if cls.__name__ == "Rectangle":
                writer = csv.DictWriter(csvFile, fieldnames=rectangle_field)
                writer.writerows(result)
            elif cls.__name__ == "Square":
                writer = csv.DictWriter(csvFile, fieldnames=square_field)
                writer.writerows(result)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from a csv file"""
        filename = cls.__name__ + ".csv"
        rectangle_field = ["id", "width", "height", "x", "y"]
        square_field = ["id", "size", "x", "y"]
        result = []
        if not os.path.exists("./{:s}".format(filename)):
            return result

        with open(filename, mode='r') as file:

            # reading the CSV file
            csvFile = csv.reader(file)

            # displayig the contents of the CSV file
            if (cls.__name__ == "Rectangle"):
                for data in csvFile:
                    new_dict = {}
                    for key, value in zip(rectangle_field, data):
                        new_dict[key] = int(value)
                    result.append(cls.create(**new_dict))
            elif (cls.__name__ == "Square"):
                for data in csvFile:
                    new_dict = {}
                    for key, value in zip(square_field, data):
                        new_dict[key] = int(value)
                    result.append(cls.create(**new_dict))

        return (result)
