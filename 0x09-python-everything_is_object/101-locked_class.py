#!/usr/bin/python3
"""Module to a locked class"""


class LockedClass():
    """Class that prevents the user from
    dynamically creating new instance attributes"""
    __slots__ = ["first_name"]
