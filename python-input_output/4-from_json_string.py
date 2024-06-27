#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function from_json_string(my_str)"""
import json


def from_json_string(my_str):
    """return an object represented by a JSON string"""
    return json.loads(my_str)
