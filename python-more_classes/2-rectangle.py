#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Rectangle"""


class Rectangle:
    """This class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initialized the data
        Args
            width (int): the width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """this method returns the rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """This method returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2
