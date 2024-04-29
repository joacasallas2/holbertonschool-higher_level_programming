#!/usr/bin/python3
# Author: Joana Casallas
def multiply_list_map(my_list=[], number=0):
    """
    return a list with all values multiplied
    by a number without using any loops.
    """
    new_list = list(map(lambda x: x * number, my_list))
    return new_list
