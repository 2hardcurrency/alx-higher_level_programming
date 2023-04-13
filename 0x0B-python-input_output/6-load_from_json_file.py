#!/usr/bin/python3
"""Contains function that creates object from json"""


import json


def load_from_json_file(filename):
    """defines the function that creates object from json"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
