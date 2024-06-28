#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a function def pascal_triangle(n)"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal's triangle of n"""
    matrix = []
    for i in range(n):
        list_row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                list_row.append(1)
            else:
                list_row.append(matrix[i-1][j-1] + matrix[i-1][j])
        matrix.append(list_row)
    return matrix
