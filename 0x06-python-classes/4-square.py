#!/usr/bin/python3
"""Defining Square with size and area considering errors"""


class Square:
    """Square Class with size, area and errors definition"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        size_mult_twice = self.__size * self.__size
        return size_mult_twice

    @property
    def size(self):
            return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
