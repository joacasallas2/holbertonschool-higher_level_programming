#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function to_json_string(my_obj)"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
