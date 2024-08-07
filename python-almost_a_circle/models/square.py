#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class define a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the data"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """prints in the stdout"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """get the size of the square"""
        return self.__width

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            list_args = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, list_args[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["size"] = self.size
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
