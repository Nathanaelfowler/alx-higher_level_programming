#!/usr/bin/python3
"""compulsory line"""


def print_square(size):
    """prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    #print("{}".format(size))
    for row in range(size):
        for col in range(size):
            print("#", end=' ')
        print()
