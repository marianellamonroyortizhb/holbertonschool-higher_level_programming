#!/usr/bin/python3
#!/usr/bin/python3
""" Square class """


class Square:
    """ Square instances """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """ Computes square area """
    def area(self):
        return self.__size * self.__size

    """ Computes square size """
    @property
    def size(self):
        return self.__size

    """ Sets square size """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Prints all """
    def my_print(self):
        if self.__size > 0:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    """ Define position property """
    @property
    def position(self):
        return self.__position

    """ Sets position """
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """ Sets list """
    def __repr__(self):
        newstring = ""
        if self.__size > 0:
            for row in range(self.__position[1]):
                newstring += "\n"
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    newstring += " "
                for column in range(self.__size):
                    newstring += "#"
                newstring += "\n"
        else:
            newstring += '\n'
        return newstring[:-1]
