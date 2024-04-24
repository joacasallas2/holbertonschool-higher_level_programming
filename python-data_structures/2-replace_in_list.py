#!/usr/bin/python3
# Author: Joana Casallas
def replace_in_list(my_list, idx, element):
    """replace an element of a list at a specific position.:
    keyword arguments:
    my_list -- The list
    idx -- The index
    element -- The element to put in idx
    If idx is negative or if idx is out of range, the function should
    not modify anything, and returns the original list
    """
    lenght = len(my_list)
    if idx < lenght and idx >= 0:
        my_list[idx] = element
    return my_list
