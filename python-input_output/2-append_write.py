#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function append_write"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        wrote = f.write(text)
    return wrote
