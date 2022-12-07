#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for replace, search in enumerate(my_list):
        if search:
            my_list[replace] += 1
    return my_list
