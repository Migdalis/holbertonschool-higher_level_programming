#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for x, y in list(a_dictionary.items()):
        if y is value:
            del (a_dictionary[x])
    return (a_dictionary)
