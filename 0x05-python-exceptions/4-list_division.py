#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final = []
    for ind in range(list_length):
        try:
            div_list = my_list_1[ind] / my_list_2[ind]
        except IndexError:
            div_list = 0
            print("out of range")
        except ZeroDivisionError:
            div_list = 0
            print("wrong type")
        finally:
            final.append(div_list)
    return final
