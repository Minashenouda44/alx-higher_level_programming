#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if not matrix:
        return None

    for subX in matrix:
        if len(subX == 0):
            print()
        for i in range(len(subX)):
            print("{:d}" .format(subX[i]),
                  end="\n" if i is len(subX) - 1 else " ")
