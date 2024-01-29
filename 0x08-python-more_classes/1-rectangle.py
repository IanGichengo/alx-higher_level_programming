#!/usr/bin/python3
""" defines class Rectangle """


class Rectangle:
    """ attributes of class rectangle """

    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle instance with width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for retrieving the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for setting the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for retrieving the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for setting the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
