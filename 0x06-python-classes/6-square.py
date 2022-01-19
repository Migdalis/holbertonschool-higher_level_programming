#!/usr/bin/python3
"""Class Square that defines a square by size"""


class Square:
    """Class used to represent a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters
        ----------
        size : int
            Size of the square
        position : a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the value of the attribute size"""
        return (self.__size)

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

    @property
    def position(self):
        """Get the value of the attribute position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Set or change the value of position and chek if the tuple is valid
        Parameters
        ----------
        value : Tuple of 2 positive integers
            Position
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(elem, int) for elem in value) or
                not all(elem >= 0 for elem in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the # character"""
        if (self.__size == 0):
            print("")
            return
        for i in range(0, self.__size):
            print("{}".format(" " * self.__position[0]), end="")
            print("{}".format("#" * self.__size))
