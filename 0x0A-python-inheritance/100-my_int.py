#!/usr/bin/python3
""" rebel integer class """


class MyInt(int):
    """
    Represents a rebel integer class with inverted equality operators.
    """

    def __eq__(self, other):
        """
        Inverts the equality operator.

        Args:
            other (int): The value to compare.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator.

        Args:
            other (int): The value to compare.

        Returns:
            bool: True if equal, False otherwise.
        """
        return super().__eq__(other)
