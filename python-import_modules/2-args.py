#!/usr/bin/python3
# Author: Joana Casallas
"""program that prints the number of and the list of its arguments"""
if __name__ == "__main__":
    from sys import argv
    lenght = len(argv)
    if lenght == 0 or lenght == 1:
        print("0 arguments.")
    elif lenght == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(lenght - 1))
        for i in range(1, lenght):
            print("{}: {}".format(i, argv[i]))
