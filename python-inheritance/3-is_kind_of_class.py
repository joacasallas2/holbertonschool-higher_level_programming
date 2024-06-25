#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """ returns True if obj is an instance of a class that inherited from"""
    if isinstance(obj, a_class):
        return True
    return False
