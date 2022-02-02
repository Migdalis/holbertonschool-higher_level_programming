#!/usr/bin/python3
"""Define a function that reads a text file"""


def read_file(filename=""):
    """Function that reads a text file in UTF8 and prints it to stdout"""

    with open(filename, encoding="utf-8") as m_file:
        print(m_file.read(), end="")
