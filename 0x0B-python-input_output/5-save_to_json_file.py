#!/usr/bin/python3
"""Contains the function that writes an object to file"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file"""
    return json.load(my_obj, filename)
