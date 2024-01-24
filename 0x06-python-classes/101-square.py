#!/usr/bin/python3
""" creation of class square """


class Square:
    """ initialises the square class """

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the value of the private attribute position.

        Returns:
        - tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the value of the private attribute position.

        Parameters:
        - value (tuple): The new position to set.
          Raises a TypeError if value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
        - int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.

        If size is equal to 0, print an empty line.
        Position should be used by adding spaces.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        String representation of the square.

        Returns:
        - str: The square as a string, with '#' characters and spaces.
        """
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.strip()


""" Test the Square class with the provided examples """
my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
