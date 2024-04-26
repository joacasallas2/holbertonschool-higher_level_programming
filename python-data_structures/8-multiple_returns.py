#!/usr/bin/python3
# Author: Joana Casallas
def multiple_returns(sentence):
    """
    return a tuple with the length of a string and its first character.
    """
    if sentence is None:
        return (0, "None")
    lenght = len(sentence)
    return (lenght, sentence[0])
