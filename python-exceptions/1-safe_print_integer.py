#!/usr/bin/python3
# Author: Joana Casallas
def safe_print_integer(value):
    """prints an integer with "{:d}".format()."""
    try:
        print("{}".format(int(value)))
    except ValueError:
        return False
    except TypeError:
        return False
    return (True)
