#!/usr/bin/python3
"""a compulsory line"""


def append_write(filename="", text=""):
    """a func. to append to a file"""
    with open(filename, "a", encoding='UTF-8') as a_file:
        afile = a_file.write(text)
        return afile
