#!/usr/bin/python3
def no_c(my_string):
    translation = {ord('c'): None, ord('C'): None}
    my_string = my_string.translate(translation)
    return my_string
