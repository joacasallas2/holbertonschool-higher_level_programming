#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function load_from_json_file(filename)"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
