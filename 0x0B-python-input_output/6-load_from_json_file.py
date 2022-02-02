#!/usr/bin/python3
"""Define a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """
        Function that creates an Object from a “JSON file”
        Parameters
        ----------
        filename : file to create an Object
    """
    with open(filename, encoding="utf-8") as my_file:
        return json.loads(my_file.read())
