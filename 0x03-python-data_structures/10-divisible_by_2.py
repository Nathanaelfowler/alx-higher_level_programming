#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list
    for idx in len(my_list):
        if my_list[idx] % 2 == 0:
            return True
        if my_list[idx] % 2 != 0:
            return False
    return new_list
