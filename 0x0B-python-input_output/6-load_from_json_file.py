#!/usr/bin/python3
""" object from a json file """


def load_from_json_file(filename):
    """ creates an object from a json file """

    import json
    """ importing ajson module to use json.load() """

    with open(filename, mode='r', encoding='utf-8') as file:

        return json.load(file)
