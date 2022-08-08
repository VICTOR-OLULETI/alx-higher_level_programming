#!/usr/bin/python3
"""
test case for square class
"""


import unittest
import os
import json
import pycodestyle
from models import square
from models.base import Base
from models.rectangle import Rectangle
from contextlib import redirect_stdout
Square = square.Square


class TestCodeFormat(unittest.TestCase):
    def test_pycodestyle(self):
        """Test for PEP-8 format"""
        sty = pycodestyle.StyleGuide(quiet=True)
        result = sty.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                "Found code style errorrors (and warnings).")

class testcases(unittest.TestCase):
    """Testing the square class"""

    def set_default(self):
        Base.__Base_objects = 0

    def test_square_instance(self):
        """Test if square instance is Rectangle
        instance or Base instance
        """
        c1 = Square(5, 2, 1, 20)
        self.assertEqual(type(c1), Square)
        self.assertFalse(type(c1) == Rectangle)
        self.assertTrue(isinstance(c1, Base))
        self.assertTrue(isinstance(c1, Rectangle))
        self.assertTrue(isinstance(c1, Square))

    def test_size(self):
        c1 = Square(1)
        c2 = Square(2, 3)
        c3 = Square(3, 4, 5)
        c4 = Square(5, 6, 7)
        c5 = Square(7, 8, 9, 10)
        self.assertEqual(c1.size, 1)
        self.assertEqual(c2.size, 2)
        self.assertEqual(c3.size, 3)
        self.assertEqual(c4.size, 5)
        self.assertEqual(c5.size, 7)

    def test_height(self):
        c1 = Square(1)
        c2 = Square(2, 3)
        c3 = Square(3, 4, 5)
        c4 = Square(5, 6, 7)
        c5 = Square(7, 8, 9, 10)

        self.assertEqual(c1.height, 1)
        self.assertEqual(c2.height, 2)
        self.assertEqual(c3.height, 3)
        self.assertEqual(c4.height, 5)
        self.assertEqual(c5.height, 7)

    def test_x(self):
        c1 = Square(1)
        c2 = Square(2, 3)
        c3 = Square(3, 4, 5)
        c4 = Square(5, 6, 7)
        c5 = Square(7, 8, 9, 10)
        self.assertEqual(c1.x, 0)
        self.assertEqual(c2.x, 3)
        self.assertEqual(c3.x, 4)
        self.assertEqual(c4.x, 6)
        self.assertEqual(c5.x, 8)


    def test_no_arg(self):
        with self.assertRaises(TypeError):
            s = Square()

    def test_invalid_args(self):
        """Testing invalld arguments for class Square"""

        # testing the width value
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("no strings")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(False)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square([1, 2])

        # testing the ValueError for the width
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)

        # testing the value x
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

        # testing the value of y
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)
    
    def test_area(self):
        """Test area"""
        c1 = Square(1)
        c2 = Square(2, 3)
        c3 = Square(3, 4, 5)
        c4 = Square(5, 6, 7)
        c5 = Square(7, 8, 9, 10)

        self.assertEqual(c1.area(), 1)
        self.assertEqual(c2.area(), 4)
        self.assertEqual(c3.area(), 9)
        self.assertEqual(c4.area(), 25)
        self.assertEqual(c5.area(), 49)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            s = Square()

    def test_size_type(self):
        """Testing the size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("no string")

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(False)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square([1, 3])

    def test_size_value(self):
        """Testing the size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_x_valuerror(self):
        """Tests for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def test_y_valueError(self):
        """Tests for y value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(5, 4, -2)

    def test_area_args(self):
        """passing an argument into the area function"""
        c1 = Square(1)
        with self.assertRaises(TypeError):
            c1.area(1)

    def test_kwargs(self):
        """Test for invalid arguments for kwargs"""
        s = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            s.update(size=[3, 4])
        with self.assertRaises(TypeError):
            s.update(x="no string")

        with self.assertRaises(ValueError):
            s.update(size=-2)
        with self.assertRaises(ValueError):
            s.update(size=0)
        with self.assertRaises(ValueError):
            s.update(x=-2)
        with self.assertRaises(ValueError):
            s.update(y=-2)

    def test_to_dict(self):
        """Tests for dictionary function"""
        c1 = Square(1)
        c2 = Square(2, 3)
        c3 = Square(3, 4, 5)

        test_c1 = c1.to_dictionary()
        test_c2 = c2.to_dictionary()
       
        self.assertTrue(type(test_c1) is dict)
        self.assertTrue(type(test_c2) is dict)

        c3.update(**test_c1)
        self.assertEqual(str(c3), str(c1))
