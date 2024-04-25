#!/usr/bin/python3
# Author: Joana Casallas
def print_matrix_integer(matrix=[[]]):
    """print a matrix of integers.
    keyword arguments:
    matrix -- the matrix to print
    """
    lenght = len(matrix)
    for i in range(lenght):
        lenght2 = len(matrix[i])
        for j in range(lenght2):
            if j != 0:
                print(end=" ")
            print("{:d}".format(matrix[i][j]), end="")
        print(end="\n")
