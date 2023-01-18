#!/usr/bin/python3
"""a compulsory line"""


import json
def to_json_string(my_obj):
    """a func. to return the JSON representation of an object (string)"""
    myobj = json.dumps(my_obj)
    return myobj
