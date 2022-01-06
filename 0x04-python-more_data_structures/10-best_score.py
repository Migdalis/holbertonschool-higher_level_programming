#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    max = 0
    for x, y in a_dictionary.items():
        if (y > max):
            max = y
            key = x
    return (key)
