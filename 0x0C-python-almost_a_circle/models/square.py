#!/usr/bin/python3
""" Define Square Class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str """

        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
