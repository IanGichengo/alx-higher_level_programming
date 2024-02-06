#!/usr/bin/python3
""" JSON representation of an object """


def to_json_string(my_obj):
    """ returns the JSON representation of an object """

    import json
    """ importing json module to use json.dumps() """

    return json.dumps(my_obj)
