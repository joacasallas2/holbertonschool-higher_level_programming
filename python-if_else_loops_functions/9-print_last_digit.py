#!/usr/bin/python3
# Author: Joana Casallas
def print_last_digit(number):
    """function that prints the last digit of a number."""
    digit = number % 10
    if number < 0:
        digit = -number % 10
    print("{}".format(digit), end="")
    return digit
