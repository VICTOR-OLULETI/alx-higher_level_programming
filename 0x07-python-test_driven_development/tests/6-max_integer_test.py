#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Set of test to validate the functionality of the function max integer"""

    def test_doc(self):
        """Validating the documentation in the file"""
        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_max(self):
        """Test normal cases without error"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
    
    def test_boolean(self):
        """Test boolean cases without error"""
        self.assertEqual(max_integer([True, False, True]), True)

    def test_strings(self):
        """Test string cases without error"""
        self.assertEqual(max_integer(['h', 'a', 'z']), 'z')

    def test_negative(self):
        """Test cases with negative integers without error"""
        self.assertEqual(max_integer([-1, -5, -1]), -1)

    def test_empty(self):
        """Test cases when the list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_enumber(self):
        """Test cases when the values have an e"""
        self.assertEqual(max_integer([1, 319e500, 5]), 319e500)

    def test_same_number(self):
        """TEst case when the number is the same"""
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)

    def test_individual_number(self):
        """Test case when only one number is in the list"""
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
