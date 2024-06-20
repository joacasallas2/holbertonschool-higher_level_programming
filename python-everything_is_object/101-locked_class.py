#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a LockedClass class"""


class LockedClass:
    """Class that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name"""
    __slots__ = ['first_name']
