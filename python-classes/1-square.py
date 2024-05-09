#!/usr/bin/python3
# Author: Joana Casallas
"""1-square

Module 1-square: define a class that define a Square

"""


class Square:
    """
     class Square that defines a square

    Args:
        size (int): The size of the square.

    Attributes:
        size (int): Private instance attribute
    """

    def __init__(self, size):
        """Initializes the data"""
        self._size = size
