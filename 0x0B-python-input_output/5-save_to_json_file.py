#!/usr/bin/pythnm3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    json.dump(my_obj, filename)
