#!/usr/bin/python3
# Author: Joana Casallas
"""
program that prints #pythoniscool, followed by a new line,
in the standard output.
"""
if __name__ == "__main__":
    __import__("os").write(1, "#pythoniscool\n".encode("UTF-8"))
