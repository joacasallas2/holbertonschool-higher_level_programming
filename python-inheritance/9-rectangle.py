#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a rectangle"""
    def __init__(self, width, height):
        """Initialize data"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area"""
        return self.__height * self.__width

    def __str__(self):
        """print in the stdout"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
