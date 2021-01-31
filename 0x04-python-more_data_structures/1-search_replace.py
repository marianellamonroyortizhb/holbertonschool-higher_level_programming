#!/usr/bin/python3
def search_replace(my_list, search, replace):
        search_list = my_list.copy()
        for ind in range(len(search_list)):
                if (my_list[ind] == search):
                        search_list[ind] = replace
        return search_list
