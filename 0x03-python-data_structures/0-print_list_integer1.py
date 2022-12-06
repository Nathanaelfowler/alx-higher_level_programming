#!/usr/bin/python3

def print_list_integer(my_list=[]):

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)

    for i in range(len(my_list)):
        print("{}".format(my_list[i]))

print_list_integer()
