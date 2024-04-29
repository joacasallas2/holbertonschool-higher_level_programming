#!/usr/bin/python3
# Author: Joana Casallas
import functools


def uniq_add(my_list=[]):
    """ add all unique integers in a list (only once for each integer)"""
    result = functools.reduce(lambda x, y: x + y, set(my_list))
    return result
