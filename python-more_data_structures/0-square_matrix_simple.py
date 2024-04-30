#!/usr/bin/python3
# Author: Joana Casallas
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_matrix = []
    for i in matrix:
        new_matrix.append([j * j for j in i])
    return new_matrix
