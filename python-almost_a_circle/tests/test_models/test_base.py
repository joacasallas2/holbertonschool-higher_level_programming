#!/usr/bin/python3
# Author: Joana Casallas
"""Tests"""

import unittest
from models.base import Base


class TestBaseAssigningID(unittest.TestCase):
    """group of tests of Base class for assigning an ID"""
    def test_auto_id_assignemt_automatically(self):
        """Test of Base() for assigning automatically an ID exists"""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_manual_id_assignemt(self):
        """Test of Base class for assigning an manual ID exists"""
        b4 = Base(12)
        b5 = Base(13)

        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 13)

if __name__ == "__main__":
    unittest.main()
