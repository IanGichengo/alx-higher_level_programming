#!/usr/bin/python3

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


""" Filename for the JSON file """
filename = "add_item.json"

if not path.exists(filename):
    save_to_json_file([], filename)

my_list = load_from_json_file(filename)

""" Append command line arguments to the list """
my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
