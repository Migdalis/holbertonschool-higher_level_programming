#!/usr/bin/python3
"""Class Rectangle that defines a rectangle by width"""


class Rectangle:
    """Class to define a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        width : int
            Width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the value of the attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set or change the value of width and chek if a value is valid
        Parameters
        ----------
        value : int
            Width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of the attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set or change the value of height and chek if a value is valid
        Parameters
        ----------
        value : int
            Height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        return (self.width * 2) + (self.height * 2)
