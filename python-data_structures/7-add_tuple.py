#!/usr/bin/python3
# Author: Joana Casallas
def add_tuple(tuple_a=(), tuple_b=()):
    """
    function that adds 2 tuples.
    Keywords arguments:
    tuple_a -- first tuple
    tuple_b -- second tuple
    Returns a tuple with 2 integers
    """
    tuple_c = (0, 0)
    if len(tuple_a) < 2:
        tuple_a += tuple_c
    if len(tuple_b) < 2:
        tuple_b += tuple_c
    
    list_values = [tuple_a[0], tuple_b[0], tuple_a[1], tuple_b[1]]
    values = [0 if i is None else i for i in list_values]
    return ((values[0] + values[1]), (values[2] + values[3]))
