#!/usr/bin/python3
"""a compulsory line"""


import json


def load_from_json_file(filename):
    """a func. to create an Object from a “JSON file”"""
    with open(filename, "r", encoding="UTF-8") as a_file:
        afile = json.loads(a_file.read())
        """return afile"""
