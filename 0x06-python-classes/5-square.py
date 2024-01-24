#!/usr/bin/python3
""" creation of class square """


class Square:
    """ initialises the square class """

    def __init__(self, size=0):

        self.size = size

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

        """ check if value is an integer """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        """ check if value is non-negative """
        if value < 0:
            raise ValueError("size must be >= 0")

        """ set the new size """
        self.__size = value

    def area(self):

        return self.__size * self.__size

    def my_print(self):

        """ if size is 0, print an empty line """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
