#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Student"""


class Student:
    """ defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialize the data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        dict_student = self.__dict__
        if attrs is None:
            return dict_student
        dict_attrs = {}
        for key in attrs:
            if hasattr(self, key):
                dict_attrs[key] = dict_student[key]
        return dict_attrs

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if len(json) == 0:
            return
        new_attrs = {}
        self.__dict__ = new_attrs
        for key in json:
            new_attrs[key] = json[key]
