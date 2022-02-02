#!/usr/bin/python3
"""Define a function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
        Function that writes an Object to a text file,
        using a JSON representation
        Parameters
        ----------
        my_obj : object to encode
        filename : file to save the JSON representation
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
