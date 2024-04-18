#!/usr/bin/python3
# Author: Joana Casallas
def fizzbuzz():
    """function that prints the numbers from 1 to 100 separated by a space."""
    for i in range(1, 101):
        if i > 1:
            print(end=", ")
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end="")
        elif i % 5 == 0:
            print("Buzz", end="")
        elif i % 3 == 0:
            print("Fizz", end="")
        else:
            print("{}".format(i), end="")
        if i == 100:
            print(end=" ")
