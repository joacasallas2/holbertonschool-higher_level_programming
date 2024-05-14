#!/usr/bin/python3
# Author: Joana Casallas
"""Define a class Node"""


class Node:
    """Define a node of a single list"""
    def __init__(self, data, next_node=None):
        """initializes the data
        Args:
            data (int): The data of the linked list node
            next_node: The next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next_node data"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node data"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a single linked list"""

    def __init__(self):
        """Initilizes the head with None
        Args:
            head (node): The head of the linked list
        """
        self.__head = None

    def __str__(self):
        """print the entire list in stdout, one node number by line"""
        nodes = []
        tmp = self.__head
        while (tmp):
            nodes.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """insert a new Node"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node and tmp.next_node.data < new.data:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
