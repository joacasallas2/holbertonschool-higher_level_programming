#!/usr/bin/python3
# Author: Joana Casallas
for i in range(0, 100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{:02}".format(i), end=", ")
