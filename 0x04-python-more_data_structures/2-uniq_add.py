#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = (list(set(my_list)))
    add = 0
    for i in unique_list:
        add += i
    return (add)
