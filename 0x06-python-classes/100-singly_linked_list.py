#!/usr/bin/python3
""" creation of class node """


class Node:
    """ initialises the node class """

    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node

    @property
    def data(self):

        return self.__data

    @data.setter
    def data(self, value):

        """ Check if value is an integer """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):

        return self.__next_node

    @next_node.setter
    def next_node(self, value):

        """ Check if value is a Node or None """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.

        Attributes:
        - head: The first node in the linked list (initially set to None).
        """
        self.head = None

    def sorted_insert(self, value):

        new_node = Node(value)
        """ If the list is empty or the new node has a smaller data value """
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            """ Find the correct position to insert the new node """
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):

        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
