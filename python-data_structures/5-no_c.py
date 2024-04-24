#!/usr/bin/python3
# Author: Joana Casallas
def no_c(my_string):
    """removes all characters c and C from a string.
    keywords arguments:
    my_string: The string
    """
    lenght = len(my_string)
    str2 = ""
    for i in range(lenght):
        if my_string[i] is not "c" and my_string[i] is not "C":
            str2 += my_string[i]
    return str2
