#!/usr/bin/python3
# Author: Joana Casallas
import sys


def safe_function(fct, *args):
    """execute a function safely."""
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
