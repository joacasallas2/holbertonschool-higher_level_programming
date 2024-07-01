#!/usr/bin/python3
# Author: Joana Casallas
"""Tests"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """group of tests of Rectangle class"""
    def setUp(self):
        "setup for test cases"
        Base._Base__nb_objects = 0

    def test_auto_id_assignemt(self):
        """Test of Rectangle() for assigning automatically an ID exists"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(1, 2)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_manual_id_assignemt(self):
        """Test of Rectangle class for assigning an manual ID exists"""
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r3.id, 12)

    def test_x_assignemt(self):
        """Test of Rectangle class for assigning an x value exists"""
        r4 = Rectangle(1, 2, 3)

        self.assertEqual(r4.x, 3)

    def test_y_assignemt(self):
        """Test of Rectangle class for assigning an y value exists"""
        r5 = Rectangle(1, 2, 3, 4)

        self.assertEqual(r5.y, 4)

if __name__ == "__main__":
    unittest.main()
