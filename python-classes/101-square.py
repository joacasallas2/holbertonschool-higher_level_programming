#!/usr/bin/python3
# Author: Joana Casallas
"""Define a Class Square"""


class Square:
    """Define a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data
        Args:
            size (int): The size of the square
            position (int): The position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the area of the square"""
        return self.size ** 2

    def my_print(self):
        """print in stdout the square with the character #"""
        if self.size == 0:
            print(end="\n")
        else:
            for i in range(self.position[1]):
                print(end="\n")
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print(end="\n")

    def __str__(self):
        """print in stdout the square with the character #"""
        for i in range(self.position[1]):
            print(end="\n")
        for i in range(self.size):
            [print(" ", end="") for j in range(self.position[0])]
            [print("#", end="") for j in range(self.size)]
            if i < self.size - 1:
                print(end="\n")
        return ""
