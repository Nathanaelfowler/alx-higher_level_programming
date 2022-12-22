#!/usr/bin/python3
"""compulsory line"""


class Square:
    """defining a class"""

    def __init__(self, size=0):
        """using a method"""
        self.__size = size

        ##This is the getter
        @property
        def size(self):
            return self.__size

        ##This is the setter
        @size.setter
        def size(self, value):
            if type(value) != int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise TypeError("size must be >= 0")
            else:
                self.__size = value

        def area(self):
            """a method for the area"""
            return int(self.__size) * int(self.__size)
