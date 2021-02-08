#!/usr/bin/python3
"""Defining Square with size and area considering errors and using setter"""


class Square:
    """Square Class with size, area and errors definition"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        size_mult_twice = self.__size * self.__size
        return size_mult_twice

    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.size != 0:
            for ind1 in range(self.position[1]):
                print()
            for ind1 in range(self.size):
                for ind2 in range(self.position[0]):
                    print(" ", end="")
                for ind2 in range(self.size):
                        print("#", end="")
                print()
        else:
            print()
