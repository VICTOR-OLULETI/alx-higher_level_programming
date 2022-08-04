#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
and then save them to a file
"""


from sys import argv
from os.path import exists


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
argc = len(argv)

py_list = []
if exists(filename):
    py_list = load_from_json_file(filename)
else:
    save_to_json_file("", filename)

if argc == 1:
    save_to_json_file(py_list, filename)
else:
    for i in range(1, argc):
        py_list.append(argv[i])
    save_to_json_file(py_list, filename)
