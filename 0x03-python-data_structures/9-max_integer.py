#!/usr/bin/python3


def max_integer(my_list=[]):

    if not my_list:
        return None

    big = 0
    for i in my_list:
        if my_list[i] > big:
            big = my_list[i]

    return big


'''

if len(my_list < 1):
return none
listCopy = my_list.copy()
listCopy.sort()

return listCopy[-1]
'''
