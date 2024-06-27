#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a script that adds all args"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_arg():
    """function that adds all args"""
    filename = "add_item.json"
    if os.path.exists(filename):
        list_args = load_from_json_file(filename)
    else:
        list_args = []
    for i in range(1, len(sys.argv)):
        list_args.append(sys.argv[i])
    save_to_json_file(list_args, filename)


if __name__ == "__main__":
    add_arg()
