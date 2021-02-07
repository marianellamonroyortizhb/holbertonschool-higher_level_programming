#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ind = 0
    for ind in range (x):
        try:
            print("{}".format(my_list[ind]), end="")
            ind = ind + 1
        except IndexError:
            break
    print("")
    return(ind)
