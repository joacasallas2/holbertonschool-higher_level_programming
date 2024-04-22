#!/usr/bin/python3
# Author: Joana Casallas
"""
program that prints all the names defined by
the compiled module hidden_4.pyc
"""
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    sorted_names = sorted(name for name in names if not str.startswith("__"))
    for name in sorted_names:
        print(name)
