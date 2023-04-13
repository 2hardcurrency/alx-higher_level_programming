#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""

import sys
import json
from os import path

save_to_json_file = __import__(5-save_to_json_file.py).save_to_json_file
load_from_json_file = __import__(6-load_from_json_file.py).load_from_json_file

json_list = []
for arg in sys.argv[1:]:
    json_list.append(arg)

filename = "add_item.json"

if path.exist(filename):
    json_list += load_from_json_file(filename)

save_to_json_file(json_list, filename)
