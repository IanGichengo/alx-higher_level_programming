#!/usr/bin/python3
""" dictionary description with simple data structure """


def class_to_json(obj):
    """ obj  is an instance of a class dict contains attributes """

    json_dict = {}

    for attr_name in dir(obj):

        if not attr_name.startswith("__"):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dict[attr_name] = attr_value
                """ add the attribute to the dictionary """

                return json_dict
