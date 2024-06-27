#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function write_file()"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        wrote = f.write(text)
    return wrote
