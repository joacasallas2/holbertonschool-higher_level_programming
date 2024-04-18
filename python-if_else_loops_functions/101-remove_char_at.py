#!/usr/bin/python3
# Author: Joana Casallas
def remove_char_at(str, n):
    """
    function that creates a copy of the string
    removing the character at the position n
    """
    new = ""
    lenght = len(str)
    for i in range(0, lenght):
        if i == n:
            continue
        new += str[i]
    return new
