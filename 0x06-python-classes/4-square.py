#!/usr/bin/python3
""" class square with defined size """


class Square:

    """ initialises new instance of the square class """
    def __init__(self, size=0):

        """ private instance attribute to store the size """
        self.__size = size

    @property
    def size(self):
        """
        Getter method to retrieve the value of the private attribute size.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):

        """ Check if value is an integer """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        """ Check if value is non-negative """
        if value < 0:
            raise ValueError("size must be >= 0")

        """ Set the new size """
        self.__size = value

        """ computes and returns the area of the square """
    def area(self):

        """ Returns the area of the square (size * size) """
        return self.__size * self.__size
