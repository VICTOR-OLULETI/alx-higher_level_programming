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
    def test_syntax_base(self):
        """
        Test that check PEP8
        (pycodestyle)
        """
        syt = pycodestyle.StyleGuide(quit=True)
        check = syt.check_files(['models/base.py'])
        self.assertEqual(
                check.total_errors, 0,
                "Found pycode style errors (and Warnings)."
        )

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
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)
