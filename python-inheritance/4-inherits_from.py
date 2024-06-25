#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function inherits_from(obj, a_class)"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that
    inherited from"""
    return isinstance(obj, a_class) and type(obj) is not a_class
