#!/usr/bin/python3
# Author: Joana Casallas
def safe_print_division(a, b):
    """divide 2 integers and print the result."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
