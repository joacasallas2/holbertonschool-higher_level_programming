#!/usr/bin/python3
# Author: Joana Casallas
def search_replace(my_list, search, replace):
    """replace all occurrences of an element by another in a new list."""
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
