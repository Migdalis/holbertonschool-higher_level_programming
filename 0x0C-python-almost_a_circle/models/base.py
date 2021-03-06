#!/usr/bin/python3
"""Class base of all other classes"""


class Base:
    """
    Define the base to the models
    Attribute:
    ----------
    __nb_objects : int
        Number of instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Construct a new Base
        Parameters:
        ----------
        id : int
            Identifier of the Base
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
