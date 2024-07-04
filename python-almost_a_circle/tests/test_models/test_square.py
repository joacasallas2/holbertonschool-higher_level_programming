#!/usr/bin/python3
# Author: Joana Casallas
"""Tests"""

import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """group of tests of Square class"""
    def setUp(self):
        "setup for test cases"
        Base._Base__nb_objects = 0

    def test_auto_id_assignemt(self):
        """Test of Square() for assigning automatically an ID exists"""
        s1 = Square(10)
        s2 = Square(1)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_manual_id_assignemt(self):
        """Test of Square class for assigning an manual ID exists"""
        s3 = Square(10, 2, 0, 12)

        self.assertEqual(s3.id, 12)

    def test_width_assignemt(self):
        """Test of Square class for assigning an width value exists"""
        s4 = Square(1, 2)

        self.assertEqual(s4.width, 1)

    def test_x_assignemt(self):
        """Test of Square class for assigning an x value exists"""
        s6 = Square(1, 2)

        self.assertEqual(s6.x, 2)

    def test_y_assignemt(self):
        """Test of Square class for assigning an y value exists"""
        s7 = Square(1, 2, 3)

        self.assertEqual(s7.y, 3)

    def test_raise_exception(self):
        """Test of Square class for raising an exception"""
        with self.assertRaises(TypeError):
            s8 = Square("1", 2)
        with self.assertRaises(TypeError):
            s9 = Square(1, "2")
        with self.assertRaises(TypeError):
            s10 = Square(1, 2, "3")
        with self.assertRaises(ValueError):
            s12 = Square(-1)
        with self.assertRaises(ValueError):
            s14 = Square(0)
        with self.assertRaises(ValueError):
            s15 = Square(1, -2)
        with self.assertRaises(ValueError):
            s16 = Square(1, 2, -3)


if __name__ == "__main__":
    unittest.main()
