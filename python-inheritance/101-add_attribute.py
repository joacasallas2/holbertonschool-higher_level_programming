#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function add_attribute()"""


def add_attribute(object, attribute, value):
    """function that adds a new attribute to an object if it is possible"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
