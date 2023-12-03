#!/usr/bin/python3
def multiple_returns(sentence):
    str_length = len(sentence)
    if str_length == 0:
        k = None
    else:
        k = sentence[0]
    new_tuple = (str_length, k)
    return new_tuple
