#!/usr/bin/python3
"""Class Square that defines a square by size"""


class Square:
    """Class used to represent a Square"""

    def __init__(self, size=0):
        """
        Parameters
        ----------
        size : int
            Size of the square
        """

        try:
            size += 0
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
            
        self.__size = size
