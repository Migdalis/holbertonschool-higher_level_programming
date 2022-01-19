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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the area square"""

        return self.__size * self.__size
