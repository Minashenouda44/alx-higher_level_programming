#!/usr/bin/python3

# a program that prints the ASCII alphabet, in lowercase,
# not followed by a new line.
# Print all the letters except q and e

for alpha in range(97, 123):
    if chr(alpha) != 'q' and chr(alpha) != 'e':
        print("{:c}" .format(alpha), end="")
