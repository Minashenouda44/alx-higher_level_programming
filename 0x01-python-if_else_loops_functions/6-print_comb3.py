#!/usr/bin/python3

# a program that prints all possible different combinations of two digits.

for d1 in range(9):
    for d2 in range(d1 + 1, 10):
        if d1 != 8:
            print("{:d}{:d}, " .format(d1, d2), end="")
        else:
            print("{:d}{:d}".format(d1, d2))
