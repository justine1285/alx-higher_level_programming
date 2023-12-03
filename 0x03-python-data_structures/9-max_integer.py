#!/usr/bin/python3
def max_integer(my_list=[]):
    list_length = len(my_list)
    if list_length == 0:
        return None
    max = my_list[0]
    for k in range(list_length):
        if my_list[k] > max:
            max = my_list[k]
    return max
