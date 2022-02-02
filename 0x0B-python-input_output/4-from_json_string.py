#!/usr/bin/python3
"""Define a function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
        Function that returns an object (Python data structure)
        represented by a JSON string
        Parameters
        ----------
        my_str : JSON string
        Returns
        -------
            An object (Python data structure)
    """
    return json.loads(my_str)
