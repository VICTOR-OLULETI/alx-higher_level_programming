#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
and then save them to a file
"""


import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
py_list = []
if os.path.exists(filename):
    py_list = load_from_json_file(filename)

if len(sys.argv) == 1:
    save_to_json_file(py_list, filename)
else:
    for i in range(1, len(sys.argv)):
        py_list.append(sys.argv[i])
    save_to_json_file(py_list, filename)
