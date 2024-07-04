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
