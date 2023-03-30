#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a/b
    except ZeroDivisionError:
        div = none
    finally:
        print("Inside result: {:d}".formet(div))
    return div

         
