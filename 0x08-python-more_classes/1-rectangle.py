#!/usr/bin/python3
"""compulsory line"""


class Rectangle:
    """defining a class"""

    def __init__(self, width=0, height=0):
        """using the 'init' method"""
        self.__width = width
        self.__height = height

        #For width:
        #getter
        @property
        def width(self):
            """defining the width"""
            return self.__width

        #setter
        @width.setter
        def width(self, value):
            """setter"""
            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        #For height:
        #getter
        @property
        def height(self):
            """defining the height"""
            return self.__height

        #setter
        @height.setter
        def height(self, value):
            """setter"""
            if type(value) != int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

