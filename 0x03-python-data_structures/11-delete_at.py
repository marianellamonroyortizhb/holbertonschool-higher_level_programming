#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    my_list_cp = my_list
    if idx > 0:
        del my_list_cp[idx]
    else:
        pass
    return (my_list_cp)
