#!/usr/bin/python3
# Author: Joana Casallas
def element_at(my_list, idx):
    """retrieve an element from a list.
    Keyword arguments:
    my_list -- The list
    idx -- The index
    If idx is negative or if idx is out of range the function return None
    """
    lenght = len(my_list)
    if idx > 0 and idx < lenght:
        return my_list[idx]
    return None
