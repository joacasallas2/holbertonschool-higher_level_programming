#!/usr/bin/python3
# Author: Joana Casallas
def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order.
    keyword arguments:
    my_list -- The list
    """
    list.reverse(my_list)
    for i in my_list:
        print("{}".format(i))
