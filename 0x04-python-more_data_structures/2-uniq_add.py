#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = (list(set(my_list)))
    partial_sum = 0
    for number in unique_list:
        partial_sum = partial_sum + number
    return(partial_sum)
