#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        operation = (sum(map(lambda x: x[0] * x[1], my_list)))
        prom = (sum(map(lambda x: x[1], my_list)))
        return (operation / prom)
    else:
        return 0
