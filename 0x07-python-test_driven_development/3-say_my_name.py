#!/usr/bin/python3
"""compulsory line"""


def say_my_name(first_name, last_name=""):
    """a function that prints My name is <first name> <last name>"""

    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {} {}".format(first_name, last_name))
    else:
        raise TypeError("first_name must be a string or last_name must be a string")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
