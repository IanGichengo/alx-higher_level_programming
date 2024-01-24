#!/usr/bin/python3
""" creation of class square """


class Square:
    """ initialises a new instance of the square class """

    def __init__(self, size=0):

        if not isinstance(size, (float, int)):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Getter method to retrieve the value of the private attribute size.

        Returns:
        - float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the value of the private attribute size.

        Parameters:
        - value (float or int): The new size to set.
          Raises a TypeError if value is not a number.
          Raises a ValueError if value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
        - float or int: The area of the square (size * size).
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison method.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if the areas of the two squares are equal
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison method.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if the areas of the two squares are not equal
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison method.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if the area of self is less than the area of other
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparison method.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if the area of self is less than
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison method.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if the area of self is greater than other
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparison method.

        Parameters:
        - other: Another Square instance.

        Returns:
        - bool: True if the area of self is greater than or equal
        """
        return self.area() >= other.area()


if __name__ == "__main__":
    # Test the Square class with comparators
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
