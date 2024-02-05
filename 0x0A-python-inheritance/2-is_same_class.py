#!/usr/bin/python3
""" logic function """


def is_same_class(obj, a_class):
    """ returns true if theobject is exactly an instance of the class """

    return type(obj) is a_class
