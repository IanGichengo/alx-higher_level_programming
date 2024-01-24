#!/usr/bin/python3
""" creation of class MagicClass """


import math


class MagicClass:
    """ initialises the MagicClass class """

    def __init__(self, radius=0):

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Computes and returns the area of the circle.

        Returns:
        - float: The area of the circle (pi * radius^2).
        """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """
        Computes and returns the circumference of the circle.

        Returns:
        - float: The circumference of the circle (2 * pi * radius).
        """
        return 2 * math.pi * self.__radius
