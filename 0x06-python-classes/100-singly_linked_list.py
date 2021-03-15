#!/usr/bin/python3
""" Node Class """


class Node:
    """ Node instances """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """ Define data """
    @property
    def data(self):
        return self.__data

    """ Assign data """
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    """ Define next node """
    @property
    def next_node(self):
        return self.__next_node

    """ Assign node pointer """
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" Linked list class """


class SinglyLinkedList:
    """ List instances """
    def __init__(self):
        self.__head = None

    """ Organize nodes """
    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    """ Assing null to last node """
    def __str__(self):
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
