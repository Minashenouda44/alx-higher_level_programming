#!/usr/bin/python3


def print_last_digit(number):

    tempNumber = abs(number)
    lastDigit = tempNumber % 10

    print("{:d}".format(lastDigit), end="")

    return lastDigit
