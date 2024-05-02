#!/usr/bin/python3
# Author: Joana Casallas
def safe_print_list(my_list=[], x=0):
    """print x elements of a list."""
    nb = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            nb += 1
        except IndexError:
            print(end="")
    print(end="\n")
    return nb
