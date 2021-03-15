#!/usr/bin/python3
""" Square class """


class Square:
    """ Square instances """
    def __init__(self, size=0):
        self.size = size

    """ Computes square area """
    def area(self):
        return self.__size * self.__size

    """ Defines size property """
    @property
    def size(self):
        return self.__size

    """ Assign value """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Compare if two elements are equal """
    def __eq__(self, other):
        return self.area() == other.area()

    """ Compare if two elements are differents """
    def __ne__(self, other):
        return self.area() != other.area()

    """ Compare if first elements is smaller """
    def __lt__(self, other):
        return self.area() < other.area()

    """ Compare if first elements is smaller or equal """
    def __le__(self, other):
        return self.area() <= other.area()

    """ Compare if first elements is bigger """
    def __gt__(self, other):
        return self.area() > other.area()

    """ Compare if first elements is bigger or equal"""
    def __ge__(self, other):
        return self.area() >= other.area()
