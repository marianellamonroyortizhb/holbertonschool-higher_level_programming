#!/usr/bin/python3
def element_at(my_list, inx):
    if (inx < 0):
        return None
    elif(inx >= len(my_list)):
        return None
    else:
        return(my_list[inx])
