#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

a = int(a)
b = int(b)

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
