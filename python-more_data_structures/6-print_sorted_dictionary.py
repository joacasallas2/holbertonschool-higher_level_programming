#!/usr/bin/python3
# Author: Joana Casallas
def print_sorted_dictionary(a_dictionary):
    """print a dictionary by ordered keys."""
    sorted_dict = sorted(a_dictionary)
    for i in sorted_dict:
        print("{}: {}".format(i, a_dictionary[i]))
