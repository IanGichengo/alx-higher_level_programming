#!/usr/bin/python3
""" object to a file using a JSON representation """


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file using a JSON representation """

    import json
    """ importing json module to use json.dump() """

    with open(filename, mode='w', encoding='utf-8') as file:

        json.dump(my_obj, file)
