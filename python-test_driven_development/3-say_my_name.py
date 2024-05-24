#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function say_my_name(first_name, last_name="")"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>
    Args:
        first_name (str): The first name
        last_name (str): The last name

    Raises:
        TypeError: first_name and last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
