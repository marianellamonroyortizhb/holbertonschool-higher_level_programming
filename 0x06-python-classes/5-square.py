#!/usr/bin/python3
"""Defining Square with size and area considering errors and using setter"""


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
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        if self.size != 0:
            for count1 in range(0, self.size):
                for count2 in range(0, self.size):
                    print("#", end="")
                print("")
        else:
            print("")
