#!/usr/bin/python3
"""a compulsory line"""


def save_to_json_file(my_obj, filename):
    """a func. to write an Object to a text file,
    using a JSON representation"""
    with open(filename, "w", encoding="UTF-8") as a_file:
        afile = a_file.write(my_obj)
