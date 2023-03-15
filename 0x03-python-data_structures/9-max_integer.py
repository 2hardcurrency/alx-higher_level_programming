#!/usr/bin/python3


def max_integer(my_list=[]):
    
    if len(my_list) == 0:
        return

    for i in my_list:
        new_list = my_list.sort()
        return new_list[-1]

