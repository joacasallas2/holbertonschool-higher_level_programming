#!/usr/bin/python3
# Author: Joana Casallas
"""
program that prints the ASCII alphabet,
in reverse order, alternating lowercase and uppercase
"""
n = 122
for i in range(0, 26, 2):
    print("{}{}".format(chr(n), chr(n - 33)), end="")
    n = n - 2
