#!/usr/bin/python3
# Author: Joana Casallas
"""Module that provides a lookup(obj) function"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
