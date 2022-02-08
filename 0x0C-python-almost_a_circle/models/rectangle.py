#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Define the models of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Construct a new Rectangle
        Parameters:
        ----------
        width : int
            width of the rectangle
        height : int
            height of the rectangle
        x : int
            posicion x in the rectangle
        y : int
            posicion y in the rectangle
        id : int
            Identifier of the Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the value of the attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set or change the value of width and chek if a value is valid
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of the attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set or change the value of height and chek if a value is valid
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the value of the attribute x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Set or change the value of x and chek if a value is valid
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of the attribute y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Set or change the value of y and chek if a value is valid
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
