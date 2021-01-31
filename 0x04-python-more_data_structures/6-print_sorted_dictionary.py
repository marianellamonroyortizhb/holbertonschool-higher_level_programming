#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for n_key in sorted(a_dictionary.keys()):
        print("{}: {}".format(n_key, a_dictionary[n_key]))
