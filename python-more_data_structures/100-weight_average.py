#!/usr/bin/python3
# Author: Joana Casallas
def weight_average(my_list=[]):
    """return the weighted average of all integers tuple (<score>, <weight>)"""
    if len(my_list) == 0:
        return 0
    num1 = 0
    num2 = 0
    for i in my_list:
        num1 += i[0] * i[1]
        num2 += i[1]
    return num1 / num2
