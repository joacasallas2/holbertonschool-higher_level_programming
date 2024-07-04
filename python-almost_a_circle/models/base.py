#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Base"""
import json


class Base:
    """This class will be the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the data"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)
