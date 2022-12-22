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

        #This is the getter
        @property
        def size(self):
            return self.__size

        #This is the setter
        @size.setter
        def size(self, value):
            if value.isdigit():
                self.__size = value
            else:
                print("Please only enter numbers for size")

        def area(self):
            """a method for the area"""
            return int(self.__size) * int(self.__size)
