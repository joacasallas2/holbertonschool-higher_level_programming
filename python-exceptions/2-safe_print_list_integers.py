#!/usr/bin/python3
# Author: Joana Casallas
def safe_print_list_integers(my_list=[], x=0):
    """print the first x elements of a list and only integers."""
    nb = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nb += 1
        except TypeError:
            print(end="")
        except ValueError:
            continue
    print(end="\n")
    return nb
