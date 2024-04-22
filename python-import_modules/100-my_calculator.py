#!/usr/bin/python3
# Author: Joana Casallas
"""
program that imports all functions from the file calculator_1.py and
handles basic operations.
"""
if __name__ == "__main__":
    import sys
    import calculator_1
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op == "+":
        print("{} {} {} = {}".format(a, op, b, calculator_1.add(a, b)))
    elif op == "-":
        print("{} {} {} = {}".format(a, op, b, calculator_1.sub(a, b)))
    elif op == "/":
        print("{} {} {} = {}".format(a, op, b, calculator_1.div(a, b)))
    elif op == "*":
        print("{} {} {} = {}".format(a, op, b, calculator_1.mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
