#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final = []
    for ind in range(list_length):
        div_list = 0
        try:
            div_list = my_list_1[ind] / my_list_2[ind]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            final.append(div_list)
    return final
