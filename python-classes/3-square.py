#!/usr/bin/python3
# AUthor: Joana Casallas
"""Define a class Square"""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """Initializes the data
        Args:
            size (int): The size of the square.
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
