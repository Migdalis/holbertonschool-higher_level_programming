#!/usr/bin/python3
"""Define a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
        Parameters
        ----------
        filename : name of the file
        text : string to appends at the end of a text file
        Returns
        -------
            The number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as m_file:
        return m_file.write(text)
