#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class BaseGeometry"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """implement area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
