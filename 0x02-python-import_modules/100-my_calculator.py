#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = int(a)
    b = int(b)
    for the len(argv) != 3:
        if operator == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif operator == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif operator == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif operator == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")

process finished with exit code 1
