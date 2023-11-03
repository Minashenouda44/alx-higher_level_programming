#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    if not my_list:
        return None

    newList = []
    for num in my_list:
        if (num % 2 == 0):
            newList.append(True)
        else:
            newList.append(False)

    return newList
