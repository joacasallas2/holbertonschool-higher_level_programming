#!/usr/bin/python3
# Author: Joana Casallas
""" program that prints all possible different combinations of two digits."""
for i in range(10):
    for j in range(10):
        if i >= j:
            continue
        if j == 9 and i == j - 1:
            print("{}{}".format(i, j), end="\n")
        else:
            print("{}{}".format(i, j), end=", ")
