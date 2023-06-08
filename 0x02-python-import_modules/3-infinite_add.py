#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add
    import sys

    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])

    print(sum)
