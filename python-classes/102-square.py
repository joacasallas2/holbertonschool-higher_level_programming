#!/usr/bin/python3
# Author: Joana Casallas
"""Define a class Square"""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """Initializes the data
        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Define de == operator to Square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define de != operator to Square"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Define de > operator to Square"""
        return self.area() > other.area()

    def __lt__(self, other):
        """Define de < operator to Square"""
        return self.area() < other.area()

    def __ge__(self, other):
        """Define de >= operator to Square"""
        return self.area() >= other.area()

    def __le__(self, other):
        """Define de <= operator to Square"""
        return self.area() <= other.area()
