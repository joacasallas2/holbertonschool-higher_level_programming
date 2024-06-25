#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a square"""
    def __init__(self, size):
        """Initialize data"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculate the area"""
        return self.__size ** 2

    def __str__(self):
        """print in the stdout"""
        return "[Square] {}/{}".format(self.__size, self.__size)
