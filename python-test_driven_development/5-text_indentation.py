#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function text_indentation(text)"""


def text_indentation(text):
    """This function prints a text with 2 new lines after each of
    these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] in (".?:"):
            print(text[i], end="\n\n")
        else:
            if text[i] == " " and text[i - 1] in (".?:"):
                continue
            print(text[i], end="")
