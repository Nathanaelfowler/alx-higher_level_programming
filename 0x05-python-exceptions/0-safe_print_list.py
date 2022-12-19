#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        length = sum([1 for i in my_list])
        for x in range(length):
            if x < length:
                print("{}".format(my_list[type(x)]))
    except Exception:
      print('Something went wrong')
