#!/usr/bin/python3
"""compulsory line"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False"""
    if type(obj) == a_class:
        return True
    else:
        return False

    if type(obj) == a_class():
        return True
    else:
        return False
