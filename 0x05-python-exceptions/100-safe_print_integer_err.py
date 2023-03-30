#!/usr/bin/python3
def safe_print_integer_err(value):
    
    try:
        if integer:
            print("{:d}\n".format())
            return true
        
    except ValueError:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return false
