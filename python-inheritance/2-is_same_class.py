#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of the specified class"""
    if type(obj) is a_class:
        return True
    return False
