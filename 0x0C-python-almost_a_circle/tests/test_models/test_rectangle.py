#!/usr/bin/python3
"""
Test for Rectangle Class
"""
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
import os


class TestcodeFormat(unittest.TestCase):
    """Tests for Base"""
    def set_default(self):
        """Sets number of objects to 0"""
        Base.__nb_objects = 0

    def test_id(self):
        """Test for positive case of Base Class id"""
        self.set_default()
        r1 = Rectangle(10, 2)
        r1.id = 1
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        r2.id = 3
        self.assertEqual(r2.id, 3)

    def test_rectangle_instance(self):
        """Checks if class Rectangle is an instance
            of Base
        """
        r = Rectangle(5, 4, 2, 6, 27)
        self.assertEqual(type(r), Rectangle)
        self.assertTrue(type(r) == Rectangle)
        self.assertFalse(type(r) == Base)

    def test_id_given(self):
        """Test id when given"""
        r3 = Rectangle(10, 4, 5, 3, 20)
        self.assertEqual(r3.id, 20)

    def test_if_wrong_arguments(self):
        """Test for wrong number arguments"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(5)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 3, 5, 6, 8, 33)


class Test_RectangleAttributes(unittest.TestCase):
    """A class to test attributs of Rectangle Class"""
    def set_default(self):
        """sets the number of objects to 0"""
        Base.__nb_objects = 0

    def test_set_attributes(self):
        """Test if the attributes are correctly matched"""
        r = Rectangle(10, 5, 1, 2, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 12)

    def test_width_and_height_greaterthan_0(self):
        """Tests if width and height > 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r3 = Rectangle(10, 2)
            r3.width = -10
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r4 = Rectangle(10, 4)
            r4.height = -10

    def test_x_and_y_greaterthan_or_equal0(self):
        """Tests if x and y is >= 0"""
        self.set_default()
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r5 = Rectangle(10, 2, 4, -5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r4 = Rectangle(10, 2, -4, 5)

    def test_private(self):
        """Test the class if we try to do a private att"""
        self.set_default()
        r6 = Rectangle(10, 2, 3, 1)
        self.assertEqual(r6.x, 3)
        with self.assertRaises(AttributeError):
            r6.__x


class Test_Rectangle_Area(unittest.TestCase):
    """Tests for the area of the Rectangle"""
    def set_default(self):
        """sets the number of objects to 0"""
        Base.__nb_objects = 0

    def test_area(self):
        """Test area"""
        self.set_default()
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r1.width = 6
        self.assertEqual(r1.area(), 12)

    def try_wrong_value(self):
        """Tests for when height is 0"""
        self.set_default()
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.height, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2.height = 0


class test_disp(unittest.TestCase):
    """Test for display methods"""
    def set_default(self):
        """sets number of objects to 0"""
        Base.__nb_objects = 0

    def test_valid_attrs_display(self):
        """checks valid attribute and display output"""
        self.set_default()
        r1 = Rectangle(3, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue(), "\n\n  ###\n  ###\n")

    def test_invalid_attrs_display(self):
        """checks invalid cases for attributes and the display output"""
        self.set_default()
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -1)
            r1.display()

    def test_display_invalid_arg(self):
        """checks invalid argument to display function"""
        self.set_default()
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 1, 1)
            r1.display(2)


class Tests_Update(unittest.TestCase):
    """Test class for update method"""
    def set_default(self):
        """sets the number of objects to 0"""
        Base.__nb_objects = 0

    def test_args_0(self):
        """passes in no argument and tests"""
        self.set_default()
        r1 = Rectangle(1, 2, 3, 4)
        r1.update()
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_args_1(self):
        """passes in 1 argument to update function"""
        self.set_default()
        r1 = Rectangle(1, 2, 3, 4)
        r1.update(20)
        self.assertEqual(r1.id, 20)

    def test_arg_2(self):
        """passes in 2 arguments to update function"""
        self.set_default()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)

    def test_arg_3(self):
        """passes in 3 arguments to update function"""
        self.set_default()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200, 300)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 300)

    def test_arg_4(self):
        """passes 4 arguments to update function"""
        self.set_default()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200, 300, 400)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 300)
        self.assertEqual(r1.x, 400)

    def test_arg_5(self):
        """passes in 5 arguments to update function"""
        self.set_default()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200, 300, 400, 500)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 300)
        self.assertEqual(r1.x, 400)
        self.assertEqual(r1.y, 500)

    def test_id_kwargs(self):
        """passes in id to function"""
        self.set_default()
        r1 = Rectangle(1, 2, 3, 4)
        r1.update(id=1000)
        self.assertEqual(r1.id, 1000)

    def test_width_kwargs(self):
        """passes in id and width to function"""
        self.set_default()
        r1 = Rectangle(1, 2, 3, 4)
        r1.update(id=10, width=20)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 20)

    def test_height_kwargs(self):
        """passes in height to function"""
        self.set_default()
        r1 = Rectangle(1, 2, 3, 4)
        r1.update(height=10)
        self.assertEqual(r1.height, 10)

    def test_x_kwargs(self):
        """passes in x to function"""
        self.set_default()
        r1 = Rectangle(1, 2, 3, 4)
        r1.update(x=20)
        self.assertEqual(r1.x, 20)

    def test_y_kwargs(self):
        """passes in y to function"""
        self.set_default()
        r1 = Rectangle(1, 2, 3, 4)
        r1.update(y=30)
        self.assertEqual(r1.y, 30)

    def test_invalid_kwargs(self):
        """passes in valid and invalid kwargs"""
        self.set_default()
        r1 = Rectangle(1, 2, 3, 4)
        r1.update(id=10, width=120, height=130, x=0, y=2, other='invalidKwarg')

        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 120)
        self.assertEqual(r1.height, 130)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 2)
        value = "'Rectangle' object has no attribute 'other'"
        with self.assertRaisesRegex(AttributeError, value):
            self.assertEqual(r1.other, 'invalidKwarg')

    def test_args_invalid(self):
        """passes in invalid arguments, value errors"""
        self.set_default()
        r1 = Rectangle(1, 2, 3, 4)

        # pass 0 to update height
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(2, 3, 0, 5)

        # pass str to update width
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(width='str')

        # pass float to height
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height=3.3)

        # pass list to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            list_value = [1, 2, 3]
            r1.update(2, list_value)

        # pass tuple to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            tuple_value = (1, 2, 3)
            r1.update(2, tuple_value)

        # pass set to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            set_value = {1, 2, 3}
            r1.update(1, set_value)

        # pass dict to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            dict_value = {'width': 2, 'x': 2, 'y': 3}
            r1.update(1, dict_value)


class Test_Dictionary_Representation(unittest.TestCase):
    """Test case class for dictionary representations"""
    def set_default(self):
        """sets the number of objects to 0"""
        Base.__nb_objects = 0

    def test_dict_with_arg(self):
        """Test to dictionary function"""
        self.set_default()
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.id, 5)
        output = "takes 1 positional argument but 2 were give"
        with self.assertRaisesRegex(TypeError, output):
            r1.to_dictionary(20)

    def test_rect_dict(self):
        """Test to dictionary function"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(5, r1.id)
        dict_value = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertDictEqual(r1.to_dictionary(), dict_value)


class TestRectangle(unittest.TestCase):
    """Test the some functionality of the rectangle class"""

    @classmethod
    def setUpClass(cls):
        """sets up several instances of the rectangle class"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(2, 3, 4)
        cls.r3 = Rectangle(5, 6, 7, 8, 9)
        cls.r4 = Rectangle(11, 12, 13, 14)

    def test_str(self):
        """Test the string method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")
        self.assertEqual(str(self.r3), "[Rectangle] (9) 7/8 - 5/6")
        self.assertEqual(str(self.r4), "[Rectangle] (3) 13/14 - 11/12")
