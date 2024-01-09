#!/usr/bin/python3
"""Defines save_to_json_file() function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    data = {}

    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            data[attr] = value
    return data
