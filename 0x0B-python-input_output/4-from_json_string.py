#!/usr/bin/python3
""" object represented by a JSON string """


def from_json_string(my_str):
    """ returns an object represented by a JSON string """

    import json
    """ importing json module to use json.loads() """

    return json.loads(my_str)
