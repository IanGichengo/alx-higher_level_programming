#!/usr/bin/python3
""" Class square with defined size """


class Square:

    """ creates attributes for class square """
    def __init__(self, size=0):

        """ check if size is an integer """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """ checks if size is a non-negative """
        if size < 0:
            raise ValueError("size must be >= 0")

        """ private instance attribute to store size """
        self.__size = size
