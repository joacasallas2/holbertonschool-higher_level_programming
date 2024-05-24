#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function print_square(size)"""


def print_square(size):
    """This function  prints a square with the character #
    Args:
        size (int): The size length of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    Return:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print(end="\n")
