#!/usr/bin/python3
# Author: Joana Casallas
def only_diff_elements(set_1, set_2):
    """ return a set of all elements present in only one set."""
    new_set = set_1 ^ set_2
    return new_set
