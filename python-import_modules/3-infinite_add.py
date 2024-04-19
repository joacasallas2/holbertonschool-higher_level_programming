#!/usr/bin/python3
# Author: Joana Casallas
"""program that prints the result of the addition of all arguments"""
if __name__ == "__main__":
    from sys import argv

    lenght = len(argv)
    sum = 0
    for i in range(1, lenght):
        sum += int(argv[i])
    print("{}".format(sum))
