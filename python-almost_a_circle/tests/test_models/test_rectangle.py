#!/usr/bin/python3
# Author: Joana Casallas
"""Tests"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleAssigningID(unittest.TestCase):
    """group of tests of Rectangle class"""
    def setUp(self):
        "setup for test cases"
        Base._Base__nb_objects = 0

    def test_auto_id_assignemt_automatically(self):
        """Test of Rectangle() for assigning automatically an ID exists"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_manual_id_assignemt(self):
        """Test of Rectangle class for assigning an manual ID exists"""
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r3.id, 12)

if __name__ == "__main__":
    unittest.main()
