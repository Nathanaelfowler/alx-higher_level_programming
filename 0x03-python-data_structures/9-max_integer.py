#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    else:
        for i in len(my_list):
            my_list.sort()
            print("Largest element is: {:d}".format(my_list[-1]))
