#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    tally = len(argv)
    if tally == 1:
        print("{} arguments.".format(tally -1))
    elif tally == 2:
        print("{} argument:".format(tally -1))
    else:
        print("{} arguments:".format(tally -1))
    for i in range(1, tally):
        print("{}: {}".format(i, argv[i]))
