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
        self.size = size

    @property
    def size(self):
        """Get the value of the attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set or change the value of size and chek if a value is valid
        Parameters
        ----------
        value : int
            Size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("{}".format('#' * self.__size))
