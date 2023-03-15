#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    if the len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    elif not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:
        a = int(a)
        b = int(b)
    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
