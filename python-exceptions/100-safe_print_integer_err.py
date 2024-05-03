#!/usr/bin/python3
# Author: Joana Casallas
import sys


def safe_print_integer_err(value):
    """print an integer."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()), file=sys.stderr)
        return False
