#!/usr/bin/python3
""" creation of class square """


class Square:
    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

    @property
    def size(self):

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

    @property
    def position(self):

        return self.__position

    @position.setter
    def position(self, value):

        """ Check if value is a tuple """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        """ Check if both elements in the tuple are positive integers """
        if not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        """ Set the new position """
        self.__position = value

    def area(self):

        return self.__size * self.__size

    def my_print(self):

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
