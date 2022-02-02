#!/usr/bin/python3
"""Define a function that returns the JSON representation"""
import json


def to_json_string(my_obj):
    """
        Function that returns the JSON representation of an object (string)
        Parameters
        ----------
        my_obj : object to encode
        Returns
        -------
            The JSON representation
    """
    return json.dumps(my_obj)
