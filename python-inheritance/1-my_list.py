#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class MyList"""


class MyList(list):
    """class that inherit from list"""
    def print_sorted(self):
        "this method prints a list, but sorted (ascending sort)"
        print(sorted(self))
