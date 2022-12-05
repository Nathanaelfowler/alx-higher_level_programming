#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        biggest = 0
        for i in len(my_list):
            if i > biggest:
                biggest = i
            return biggest
