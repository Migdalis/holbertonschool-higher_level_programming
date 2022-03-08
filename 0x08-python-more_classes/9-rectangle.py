#!/usr/bin/python3
"""Class Rectangle that defines a rectangle"""


class Rectangle:
    """Class to define a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        width : int
            Width of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return (0)
        return (self.width * 2) + (self.height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance"""
        return cls(size, size)

    def __str__(self):
        """Return a representation printeable of rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rep = []
        for i in range(self.height):
            if i == self.height - 1:
                rep.append("{}".format(str(self.print_symbol) * self.width))
                break
            rep.append("{}\n".format(str(self.print_symbol) * self.width))
        return ("".join(rep))

    def __repr__(self):
        """Representation of the rectangle"""
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")

    def __del__(self):
        """Print a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
