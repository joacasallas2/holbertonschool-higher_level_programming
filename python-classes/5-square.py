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
        return self.size ** 2

    def my_print(self):
        """print in stdout the square with the character #"""
        if self.size == 0:
            print(end="\n")
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print(end="\n")
