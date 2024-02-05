#!/usr/bin/python3
""" logical function """


def inherits_from(obj, a_class):
    """ true if the object is an instance of a class inherited """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
