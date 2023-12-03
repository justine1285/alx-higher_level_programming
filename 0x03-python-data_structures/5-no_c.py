#!/usr/bin/python3
def no_c(my_string):
    brand_new_string =  ""
    for char in my_string:
        if (char != 'c') and (char != 'C'):
            brand_new_string += char
    return (brand_new_string)
