#!/usr/bin/python3
"""
Class Node that definesa a node
of a singly linked list by:
Private instance attribute data
Private instance attribute: next_node
Istanctiation with data and next_node.

"""


class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for private attribute data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for privated attribute data"""
        if (type(value) is not int):
            raise (TypeError("data must be an integer"))
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter for private attribute next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for private attribute next_node"""
        if (value is not None) and (not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list with private instance attribute head"""
    def __init__(self):
        """Construct for the head of the linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts value in a sorted list"""
        new_node = Node(value)
        if (self.__head is None):
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        curr = self.__head
        while (value >= curr.data):
            prev = curr
            if curr.next_node:
                curr = curr.next_node
            else:
                curr.next_node = new_node
                return
        prev.next_node = new_node
        new_node.next_node = curr

    def __str__(self):
        """Prints the singly linked list"""
        str_value = ""
        curr = self.__head
        while (curr):
            str_value += str(curr.data) + "\n"
            curr = curr.next_node
        return str_value[:-1]
