#!/usr/bin/python3
def no_c(my_string):
    new_string = [x for x in my_string if x not in 'cC']
    return ("".join(new_string))
