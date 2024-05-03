#!/usr/bin/python3
# Author: Joana Casallas
import sys


def safe_print_integer_err(value):
    """print an integer."""
    exc_type, exc_obj, tb = sys.exc_info()
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(exc_obj), file=sys.stderr)
        return False
