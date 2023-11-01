#!/usr/bin/python3

# a function that prints a string in uppercase followed by a new line.

def uppercase(input_str):
    result_str = ""

    for c in input_str:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        result_str += c

    print("{}".format(result_str))


'''
def uppercase(str):

    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{:c}" .format(c), end="")
    print("")
'''
