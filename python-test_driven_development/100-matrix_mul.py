#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides the function matrix_mul(m_a, m_b)"""


def matrix_mul(m_a, m_b):
    """This function multiplies 2 matrices

    Args:
        m_a(list of list of int/float): the firs matrix
        m_b(list of list of int/float): The second matrix

    Raises:
        TypeError: If m_a or m_b is not a list of lists
        ValueError: If m_a or m_b is empty
        TypeError: If elements of m_a or m_b are not integers or floats
        TypeError: If rows of m_a or m_b are not of the same size
        ValueError: If m_a and m_b can't be multiplied

    Return:
        list of list of int/float: The result of the matrix multiplication
    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if elements of m_a and m_b are lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are non-empty
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    # Check if all elements in m_a and m_b are either integers or floats
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if m_a or m_b is not a rectangle
    if any(len(m_a[0]) != len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(m_b[0]) != len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if m_a and m_b can’t be multiplied
    if len(m_b) != len(list(zip(*m_a))):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = ([[sum(a * b for a, b in zip(a_row, b_col))for b_col in zip(*m_b)]
            for a_row in m_a])
    return m_c
