#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= range(len(my_list)):
        return my_list
    else:
        for i in range(len(my_list)):
            my_list[i] = []
    return my_list[i]
