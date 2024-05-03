#!/usr/bin/python3
# Author: Joana Casallas
def raise_exception_msg(message=""):
    """raise a name exception with a message"""
    try:
        raise Exception
    except Exception:
        print("{}".format(message))
