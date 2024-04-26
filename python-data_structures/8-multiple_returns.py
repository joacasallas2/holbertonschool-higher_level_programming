#!/usr/bin/python3
# Author: Joana Casallas
def multiple_returns(sentence):
    """
    return a tuple with the length of a string and its first character.
    """
    lenght = len(sentence)
    if sentence is None:
        return (lenght, None)
    return (lenght, sentence[0])
