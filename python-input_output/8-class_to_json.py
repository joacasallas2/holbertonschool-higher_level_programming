#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a a function class_to_json(obj)"""
import json


def class_to_json(obj):
    """ returns the dictionary description with simple data structure"""
    dict_obj = obj.__dict__
    json_str = json.dumps(dict_obj)
    json_dict = json.loads(json_str)
    return json_dict
