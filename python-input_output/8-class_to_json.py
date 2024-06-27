#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a a function class_to_json(obj)"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure"""
    dict_obj = obj.__dict__
    return dict_obj
