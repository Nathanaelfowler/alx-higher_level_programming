#!/usr/bin/python3
"""a compulsory line"""


def read_file(filename=""):
    """a func. to read a file"""
    with open(filename, "r", encoding="UTF-8") as a_file:
       afile = a_file.read()
       print(afile, end="")
