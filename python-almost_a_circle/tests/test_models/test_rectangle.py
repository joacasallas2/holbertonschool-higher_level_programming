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

    def test_str(self):
        """Test __str__()"""
        r19 = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print(r19)
        finally:
            sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display(self):
        """Test display()"""
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

    def test_to_dictionary(self):
        """Test to_dictionary method in Rectangle class"""
        r24 = Rectangle(10, 2, 1, 9)
        r24_dictionary = r24.to_dictionary()
        expected_output = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r24_dictionary, expected_output)

    def test_update(self):
        """Test update method in Rectangle class"""
        r25 = Rectangle(10, 10, 10, 10)
        r25.update(89)
        expected_output = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(str(r25), expected_output)

        r26 = Rectangle(10, 10, 10, 10)
        r26.update(89, 2)
        expected_output = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(str(r26), expected_output)

        r27 = Rectangle(10, 10, 10, 10)
        r27.update(89, 2, 3)
        expected_output = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(str(r27), expected_output)

        r28 = Rectangle(10, 10, 10, 10)
        r28.update(89, 2, 3, 4)
        expected_output = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(str(r28), expected_output)

        r29 = Rectangle(10, 10, 10, 10)
        r29.update(89, 2, 3, 4, 5)
        expected_output = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(str(r29), expected_output)

        r30 = Rectangle(10, 10, 10, 10)
        r30.update()
        expected_output = "[Rectangle] (6) 10/10 - 10/10"
        self.assertEqual(str(r30), expected_output)

    def test_create(self):
        """Test create method in Rectangle class"""
        r31 = Rectangle(3, 5, 1)
        r31_dictionary = r31.to_dictionary()
        r32 = Rectangle.create(**r31_dictionary)
        expected_output = "[Rectangle] (1) 1/0 - 3/5"
        self.assertEqual(str(r32), expected_output)

    def test_save_to_file(self):
        """Test save_to_file method in Rectangle class"""
        r33 = Rectangle(10, 7, 2, 8)
        r34 = Rectangle(2, 4)
        Rectangle.save_to_file([r33, r34])
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            with open("Rectangle.json", "r") as file:
                print(file.read())
        finally:
            sys.stdout = sys.__stdout__
        expected_output = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

        Rectangle.save_to_file([])
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            with open("Rectangle.json", "r") as file:
                print(file.read())
        finally:
            sys.stdout = sys.__stdout__
        expected_output = '[]\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

        Rectangle.save_to_file(None)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            with open("Rectangle.json", "r") as file:
                print(file.read())
        finally:
            sys.stdout = sys.__stdout__
        expected_output = '[]\n'
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
