#!/usr /bin/python3
""" class square with defined size """


class Square:

    """ initialises a new instance of the square class """
    def __init__(self, size=0):

        """ private instance attribute to store the size """
        self.__size = size

        """ getter method to retrieve the value of the private attribute"""
    @property
    def size(self):

        """ Returns the size of the square """
        return self.__size

    """ setter method to set the value of the private attribute size """
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
            return self.__size * self.__size

    """ prints the square with the character "#' to stdout """
    def my_print(self):

        """ If size is 0, print an empty line """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
