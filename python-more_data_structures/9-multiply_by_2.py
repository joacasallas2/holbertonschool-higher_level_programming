#!/usr/bin/python3
# Author: Joana Casallas
def multiply_by_2(a_dictionary):
    """return a new dictionary with all values multiplied by 2"""
    new_dictionary = {}
    for i in a_dictionary:
        new_dictionary[i] = a_dictionary[i] * 2
    return new_dictionary
