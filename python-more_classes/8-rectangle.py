#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Rectangle"""


class Rectangle:
    """This class defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialized the data
        Args
            width (int): the width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def my_print(self):
        """print in stdout the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return '\n'.join(str(self.print_symbol) *
                             self.width for _ in range(self.height))

    def __str__(self):
        """prints a rectangle using '#'"""
        return f"{self.my_print()}"

    def __repr__(self):
        """recreate a new instance by using eval()"""
        return f"Rectangle({self.width}, {self.height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
