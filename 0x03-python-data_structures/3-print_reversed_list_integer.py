#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    idx = len(my_list)
    for item in range(idx - 1, -1, -1):
        if not isinstance(my_list[item], int):
            continue
        print("{:d}".format(my_list[item]))
