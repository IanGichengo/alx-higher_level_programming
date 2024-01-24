#!/usr/bin/python3
""" creation of class node """


class Node:
    """ initialises the node class """
    def __init__(self, data, next_node=None):

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Getter method to retrieve the value of the attribute """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter method to set the value of the private attribute data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Getter method to retrieve the value of the private attribute """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Setter method to set the value of the private attribute """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" creation of class SinglyLinkedList """


class SinglyLinkedList:
    """ initialises a new instance of the SinglyLinkedList class """
    def __init__(self):

        self.__head = None

    def __str__(self):
        """ String representation of the linked list """
        nodes = []
        node = self.__head
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """ Inserts a new Node into the correct sorted position in the list """
        new_node = Node(value)
        if self.__head is None:
            """ If the list is empty, set the new node as the head """
            self.__head = new_node
        elif value < self.__head.data:
            """ If the new node has a smaller data value than the head """
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            """ Find the correct position to insert the new node """
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node
