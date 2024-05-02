#!/usr/bin/python3
# Author: Joana Casallas
def complex_delete(a_dictionary, value):
    """delete keys with a specific value in a dictionary."""
    for k, v in a_dictionary.copy().items():
        if v == value:
            del a_dictionary[k]
    return a_dictionary
