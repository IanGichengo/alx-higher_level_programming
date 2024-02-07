#!/usr/bin/python3
""" dictionary description with simple data structure """


def class_to_json(obj):
    """ obj  is an instance of a class dict contains attributes """

    ian_dict = {}
    for key, value in obj.__dict__.items():
        ian_dict[key] = value

        return ian_dict
