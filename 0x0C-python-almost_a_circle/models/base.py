#!/usr/bin/python3
""" the base for other classes in the project """


class Base:
    """Base class for managing ids."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
