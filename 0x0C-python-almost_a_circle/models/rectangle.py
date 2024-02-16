#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.__validate_int_value("width", value)
        self.__validate_positive_value("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.__validate_int_value("height", value)
        self.__validate_positive_value("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self.__validate_int_value("x", value)
        self.__validate_non_negative_value("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self.__validate_int_value("y", value)
        self.__validate_non_negative_value("y", value)
        self.__y = value

    def __validate_int_value(self, name, value):
        """Validate if value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    def __validate_positive_value(self, name, value):
        """Validate if value is positive."""
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def __validate_non_negative_value(self, name, value):
        """Validate if value is non-negative."""
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Calculate area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return string representation of Rectangle."""
        return f

    def update(self, *args, **kwargs):
        """Update attributes of the rectangle."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
