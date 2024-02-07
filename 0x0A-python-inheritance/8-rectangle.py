#!/usr/bin/python3
""" inheritance in play """


class BaseGeometry:
    def area(self):
        """
        Placeholder method for computing the area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is a positive integer.

        Args:
            name (str): The name of the attribute being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not positive.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Private attributes for width and height
        self.__width = 0
        self.__height = 0
        # Validate width and height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Assign width and height
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
