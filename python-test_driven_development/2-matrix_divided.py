#!/usr/bin/python3
# Author: Joana Casallas
"""
This module provides a function matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    Args:
        matrix (list): must be a list of lists of integers or floats
        div (integer or float): The division number

    Return: A new matrix
    """
    if not isinstance(div, (int, float)) or div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or matrix is None or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    lenght = len(matrix[0])
    for i in matrix:
        if not isinstance(i, (list)):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != lenght:
            raise TypeError(
                "Each row of the matrix must have the same size")
        for num in i:
            if not isinstance(num, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of \
integers/floats")
    return list(list(round((num / div), 2) for num in i) for i in matrix)
