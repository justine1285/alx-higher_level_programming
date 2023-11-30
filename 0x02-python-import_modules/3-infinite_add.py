#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    tally = len(argv)
    for i in range(1, tally):
        sum += int(argv[i])
    print("{}".format(sum))
