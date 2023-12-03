#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1 = [tuple_a[k] if k < len(tuple_a) else 0 for k in range(2)]
    list2 = [tuple_b[k] if k < len(tuple_b) else 0 for k in range(2)]

    sum_0 = list1[0] + list2[0]
    sum_1 = list1[1] + list2[1]
    new_tuple = (sum_0, sum_1)

    return (new_tuple)
