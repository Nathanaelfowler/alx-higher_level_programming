#!/usr/bin/python3
"""a compulsory line"""


import json


def from_json_string(my_str):
    """a func. that returns an object (Python data structure) represented by a JSON string"""
    mystr = json.loads(my_str)
    return mystr
