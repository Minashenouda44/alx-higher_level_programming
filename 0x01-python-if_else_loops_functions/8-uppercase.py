#!/usr/bin/python3

# a function that prints a string in uppercase followed by a new line.

def uppercase(str):
    for i in range(len(str)):
        char = ord(str[i])
        if char >= 97 and char <= 122:
            char = char - 32
        print("{}".format(chr(char)), end="")
    print()


'''
def uppercase(str):

    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{:c}" .format(c), end="")
    print("")
'''
