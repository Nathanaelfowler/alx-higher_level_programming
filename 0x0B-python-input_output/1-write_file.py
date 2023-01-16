#!/usr/bin/python3
"""a compulsory line"""


def write_file(filename="", text=""):
    """a func. that writes to a file"""
    with open(filename, "w", encoding="UTF-8") as a_file:
        afile = a_file.write(text)
        print(afile, end="")
        count = a_file.tell()
        return count
