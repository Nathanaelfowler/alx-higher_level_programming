#!/usr/bin/python3
"""compulsory line"""


class Square:
    """defining a class"""

    def __init__(self, size=0):
        """using a method"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
