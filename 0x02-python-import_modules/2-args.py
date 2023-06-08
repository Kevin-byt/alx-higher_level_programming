#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    ele = len(sys.argv) - 1
    if ele == 0:
        print("{} arguments.".format(ele))
    elif ele == 1:
        print("{} argument:".format(ele))
    else:
        print("{} arguments:".format(ele))

    for a in range(1, len(sys.argv)):
        print("{}: {}".format(a, sys.argv[a]))
