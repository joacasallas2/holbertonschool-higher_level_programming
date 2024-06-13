#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a program that solves the N queens problem."""
import sys


def validate_args():
    """Validate the size argument to create the chessboard"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if size < 4:
        print("N must be at least 4")
        exit(1)
    return size


def put_queens(size, row, solution, d, d2, v):
    """Place the queen in the vector and return solutions"""
    if size == row:
        return [solution.copy()]
    solutions = []
    for col in range(size):
        dg = col - row
        dg2 = col + row
        if col in v or dg in d or dg2 in d2:
            continue
        solution.append([row, col])
        v.add(col)
        d.add(dg)
        d2.add(dg2)
        solutions += put_queens(size, row + 1, solution, d, d2, v)
        solution.pop()
        v.remove(col)
        d.remove(dg)
        d2.remove(dg2)
    return solutions


def n_queens(*args):
    """Program that search the solutions for n queens problem"""
    size = validate_args()
    solutions = put_queens(size, 0, solution=[], d=set(), d2=set(), v=set())
    for sol in solutions:
        print(sol)


n_queens()
