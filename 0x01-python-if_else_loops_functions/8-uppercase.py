#!/usr/bin/python3
def uppercase(str):
    for k in str:
        temp = k
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(k) - 32)
        print("{}".format(temp), end='')
    print()
