#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in a list"""

    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    elif max(list_of_integers) == list_of_integers[0]:
        aux = list_of_integers.copy()
        aux.remove(list_of_integers[0])
        return max(aux)
    return max(list_of_integers)
