#!/usr/bin/python3


def remove_char_at(str, n):

    strCpy = ""

    for x, c in enumerate(str):
        if x != n:
            strCpy += c

    return strCpy
