#!/usr/bin/python3
""" contains a script that adds all arguments """


import sys
import json

""" Import the custom functions from other files """
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

"""Try to load the list from the file """
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)


save_to_json_file(my_list, filename)
