#!/usr/bin/python3
""" class square with defined size """


class Square:

    """ initialises a niew instance of the square class """
    def __init__(self, size=0):

        """ check if size is an integer """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """ Check if size is non-negative """
        if size < 0:
            raise ValueError("size must be >= 0")

        """ Private instance attribute to store the size """
        self.__size = size

        """ computes and returns the area of the square """
    def area(self):

        """ Returns the area of the square (size * size) """
        return self.__size * self.__size
