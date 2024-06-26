#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function read_file()"""


def read_file(filename=""):
    """read a text file (UTF8) and print it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
