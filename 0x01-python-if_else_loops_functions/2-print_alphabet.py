#!/usr/bin/python3

# a program that prints the ASCII alphabet, in lowercase,
# not followed by a new line.

for alpha in range(97, 123):
    print("{:c}" .format(alpha), end="")
