#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class MyInt"""


class MyInt(int):
    """MyInt has == and != operators inverted"""
    def __init__(self, value):
        """init data"""

    def __eq__(self, value) -> bool:
        return super().__ne__(value)

    def __ne__(self, value) -> bool:
        return super().__eq__(value)
