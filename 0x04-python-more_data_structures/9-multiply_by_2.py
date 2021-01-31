#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    double = {}
    for ind in a_dictionary:
        double[ind]= 2 * a_dictionary[ind]
    return double
