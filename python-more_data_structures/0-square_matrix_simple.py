#!/usr/bin/python3
# Author: Joana Casallas
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([j * j for j in matrix[i]])
    return new_matrix
