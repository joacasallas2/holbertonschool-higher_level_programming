#!/usr/bin/python3
# Author: Joana Casallas
def raise_exception():
    """raise a type exception."""
    try:
        raise Exception
    except Exception:
        print("Exception has been raised")
