#!/usr/bin/python3
"""Defining Square with size and area considering errors"""


class Square:
    """Square Class with size, area and errors definition"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        self_mult_twice = self.__size * self.__size
        return self_mult_twice
