#!/usr/bin/python3
""" Define class base """


class Base:
    """ Define class base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Define constructor """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
