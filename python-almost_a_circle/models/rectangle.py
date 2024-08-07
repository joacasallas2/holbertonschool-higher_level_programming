#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Define a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the data"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle with the character #"""
        for i in range(self.y):
            print(end="\n")
        for i in range(self.height):
            for k in range(self.x):
                print(end=" ")
            for j in range(self.width):
                print("#", end="")
            print(end="\n")

    def __str__(self):
        """prints in stdout the Rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        list_args = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, list_args[i], arg)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["width"] = self.width
        my_dict["height"] = self.height
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
