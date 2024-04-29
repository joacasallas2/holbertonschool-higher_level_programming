#!/usr/bin/python3
# Aurthor: Joana Casallas
def common_elements(set_1, set_2):
    """return a set of common elements in two sets."""
    new_set = (x for x in set_1 if x in set_2)
    return new_set
