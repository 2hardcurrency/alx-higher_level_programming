#!/usr/bin/python3
"""
contains the json str function
"""


import json


def from_json_string(my_str):
    """ returns an object  represented by a JSON string:"""
    return json.load(my_str)
