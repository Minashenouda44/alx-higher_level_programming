#!/usr/bin/python3


def print_list_integer(my_list=[]):

    if not my_list:
        return None

    for l in my_list:
        print("{:d}" .format(l))
