#!/usr/bin/python3
# Author: Joana Casallas
"""
0-add_integer module
This module provides a function add_integer(a, b), and ensures that its two
arguments are integers or floats and converts them to integers if necessary.
"""


def add_integer(a, b=98):
    """
    add two integers or integers casted from floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # Cast to integers if they are floats
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
