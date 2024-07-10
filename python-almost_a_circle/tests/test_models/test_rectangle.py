#!/usr/bin/python3
# Author: Joana Casallas
"""Tests"""

import unittest
import io
import sys
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

    def test_width_assignemt(self):
        """Test of Rectangle class for assigning an width value exists"""
        r4 = Rectangle(1, 2)

        self.assertEqual(r4.width, 1)

    def test_height_assignemt(self):
        """Test of Rectangle class for assigning an height value exists"""
        r5 = Rectangle(1, 2, 3, 4)

        self.assertEqual(r5.height, 2)

    def test_x_assignemt(self):
        """Test of Rectangle class for assigning an x value exists"""
        r6 = Rectangle(1, 2, 3)

        self.assertEqual(r6.x, 3)

    def test_y_assignemt(self):
        """Test of Rectangle class for assigning an y value exists"""
        r7 = Rectangle(1, 2, 3, 4)

        self.assertEqual(r7.y, 4)

    def test_raise_exception(self):
        """Test of Rectangle class for raising an exception"""
        with self.assertRaises(TypeError):
            r8 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r9 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r10 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r11 = Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            r12 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r13 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r14 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r15 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r16 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r17 = Rectangle(1, 2, 3, -4)

    def test_area_exists(self):
        """Test area() exists"""
        r18 = Rectangle(3, 2)
        self.assertEqual(r18.area(), 6)

    def test_str_exists(self):
        """Test __str__() exists"""
        r19 = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(r19)
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_exists(self):
        """Test display() exists"""
        r20 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            r20.display()
        finally:
            sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

        r21 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            r21.display()
        finally:
            sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

        r22 = Rectangle(2, 3, 2)
        expected_output = "  ##\n  ##\n  ##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            r22.display()
        finally:
            sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

        r23 = Rectangle(2, 3, 0, 2)
        expected_output = "\n\n##\n##\n##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            r23.display()
        finally:
            sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def to_dictionary_exists(self):
        """Test to_dictionary() exists"""
        r24 = Rectangle(10, 2, 1, 9)
        r24_dictionary = r24.to_dictionary()
        print(r24_dictionary)
        expected_output = "{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.assertEqual(captured_output.getvalue(), expected_output)
        self.assertEqual(captured_output.getvalue(), expected_output)

    def to_update_exists(self):
        """Test update() exists"""
        r25 = Rectangle(10, 10, 10, 10)
        r25.update(89)
        print(r25)
        expected_output = "[Rectangle] (1) 10/10 - 10/10\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
