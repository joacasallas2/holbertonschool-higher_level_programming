#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function inherits_from(obj, a_class)"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited from"""
    if type(obj) != a_class:
        return True
    return False
