#!/usr/bin/python3
"""a compulsory line"""


import json


def save_to_json_file(my_obj, filename):
    """a func. to write an Object to a text file,
    using a JSON representation"""
    myobj = json.dumps(my_obj)
    with open(filename, "w", encoding="UTF-8") as a_file:
        a_file.write(myobj)
