#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    wt_y = 0
    for x, y in my_list:
        sum += (x * y)
        wt_y += y
    return (sum / wt_y)
