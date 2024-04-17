#!/usr/bin/python3
# Author: Joana Casallas
"""program that prints numbers from 0 to 99."""
for i in range(0, 100):
    if i / 10 < 1:
        print("0", end="")
    if i == 99:
        print("{}".format(i), end="\n")
    else:
        print("{}".format(i), end=", ")
