#!/usr/bin/python3
# Author: Joana Casallas
def new_in_list(my_list, idx, element):
    """
    replaces an element in a list at a specific position
    without modifying the original list.
    keywords arguments:
    my_list -- The list
    idx -- The index
    element -- the value to replace in
    If idx is negative or idx is out of range, the function should return
    a copy of the original list
    """
    list_copy = []
    lenght = len(my_list)
    for i in range(lenght):
        if i == idx:
            list_copy.append(element)
        else:
            list_copy.append(my_list[i])
    return list_copy
