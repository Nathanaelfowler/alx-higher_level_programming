#!/usr/bin/python3
"""a compulsory line"""


def write_file(filename="", text=""):
    """a func. that writes to a file"""
    with open(filename, "w") as a_file:
        afile = a_file.write(text)
        return afile
