#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    new_list = list(my_list)
    for idx in len(my_list):
        if new_list[idx] % 2 == 0:
            return True
        if new_list[idx] % 2 != 0:
            return False
    return new_list
