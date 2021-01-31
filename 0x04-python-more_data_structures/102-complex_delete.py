#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for n_key in list(a_dictionary.keys()):
        if a_dictionary[n_key] == value:
            del a_dictionary[n_key]
    return a_dictionary
