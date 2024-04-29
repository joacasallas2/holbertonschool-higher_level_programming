#!/usr/bin/python3
# Author: Joana Casallas
def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    if a_dictionary is None:
        return None
    max_value = 0
    for k, v in a_dictionary.items():
        if v > max_value:
            max_value = v
            key = k
    return key
