#!/usr/bin/python3
"""Define a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
        Parameters
        ----------
        filename : name of the file to write
        text : string to write in the file
        Returns
        -------
            The number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as m_file:
        return m_file.write(text)
