#!/usr/bin/python3
"""
The tests for Base Class
"""
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Tests for base class
    """
    def test_base(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id2_base(self):
        b = Base()
        c = Base()
        self.assertEqual(b.id, 2)
        self.assertEqual(c.id, 3)

    def test_id_exits(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_when_positive(self):
        """
        Test for Base class id
        """
        base_instance = Base(10)
        self.assertEqual(base_instance.id, 10)
        base_instance = Base(20)
        self.assertEqual(base_instance.id, 20)
        base_instance = Base(30)
        self.assertEqual(base_instance.id, 30)

    def test_id_when_negative(self):
        """
        Test for Base class id
        """
        base_instance = Base(-10)
        self.assertEqual(base_instance.id, -10)
        base_instance = Base(-20)
        self.assertEqual(base_instance.id, -20)
        base_instance = Base(-30)
        self.assertEqual(base_instance.id, -30)

    def test_id_is_none(self):
        """
        Test when id is None or empty
        """
        base_instance = Base()
        self.assertEqual(base_instance.id, 4)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 5)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instance_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_string_id(self):
        """
        setting id to string
        """
        base_instance = Base("Sam")
        self.assertEqual(base_instance.id, "Sam")
        base_instance = Base("Vic")
        self.assertEqual(base_instance.id, "Vic")

    def test_to_dictionaryy(self):
        """
        Tests for to_json_string method
        """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1_to_dict = r1.to_dictionary()
        self.assertEqual(type(r1_to_dict), dict)

    def test_empty_to_json_string(self):
        """
        Test when an empty string is passed into to_json_string function
        """
        empty_data = []
        empty_data_json = Base.to_json_string(empty_data)
        self.assertEqual(empty_data_json, "[]")

    def test_none_to_json_string(self):

        empty_data = None
        empty_data_json = Base.to_json_string(empty_data)
        self.assertEqual(empty_data_json, "[]")

    def test_to_json2_string(self):
        """
        Test to_json_string function
        """
        rect_data = {'id': 31, 'x': 14, 'y': 10, 'width': 5, 'height': 5}
        json_data = Base.to_json_string([rect_data])

        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
                json_data,
                '{["id": 31, "x": 14, "y": 10, "width": 5, "height": 5]}'
                )

    def test_base_to_json_string(self):

        data = {'id': 12 }
        data_to_string = Base.to_json_string([data])
        self.assertTrue(isinstance(data_to_string, str))

    def test_create(self):
        """
        Test create method
        """
        with self.assertRaises(TypeError) as msg:
            r1 = Rectangle.create('string')

        self.assertEqual(
                "Base.create() takes 1 positional argument but 2 were given",
                str(msg.exception)
        )


if __name__ == "__main__":
    unittest.main()
