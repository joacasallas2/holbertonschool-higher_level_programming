#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Base"""
import json
import os
import turtle


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write(cls.to_json_string([]))
            else:
                list_dicts = []
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        new_instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                data = cls.from_json_string(f.read())
                list_instances = []
                for dictionary in data:
                    list_instances.append(cls.create(**dictionary))
            return list_instances
        return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares
        using the Turtle graphic"""
        screen = turtle.Screen()
        screen.title("Draw Rectangles and Squares")
        pen = turtle.Turtle()
        pen.speed(1)
        def draw_shape(pen, x, y, width, height):
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.forward(width)
            pen.left(90)
            pen.forward(height)
            pen.left(90)
            pen.forward(width)
            pen.left(90)
            pen.forward(height)
            pen.left(90)
            pen.penup()

        for rect in list_rectangles:
            draw_shape(pen, rect.x, rect.y, rect.width, rect.height)
        for square in list_squares:
            draw_shape(pen, square.x, square.y, square.width, square.height)

        screen.mainloop()
