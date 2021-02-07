#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ind = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            ind += 1
        except (TypeError, ValueError):
            continue
    print("")
    return ind
