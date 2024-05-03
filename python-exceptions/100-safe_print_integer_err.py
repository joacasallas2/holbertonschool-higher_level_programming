#!/usr/bin/python3
# Author: Joana Casallas
import sys


def safe_print_integer_err(value):
    """print an integer."""
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except TypeError:
        sys.stderr.write("TypeError")
        return False
