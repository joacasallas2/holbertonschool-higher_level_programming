#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y * y, x)), matrix))
    # return [[j * j for j in i] for i in matrix]
