#!/usr/bin/python3
def safe_print_division(a, b)

try:
    print(f"{:d}".format(a/b))
except ZeroDivisionError:
    print("None")

finally:
    print(f"{:d}.formet(a/b))

         
