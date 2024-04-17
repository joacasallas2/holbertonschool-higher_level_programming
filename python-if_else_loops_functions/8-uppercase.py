#!/usr/bin/python3
# Author: Joana Casallas
def uppercase(str):
    """ function that prints a string in uppercase followed by a new line."""
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print(end="\n")
