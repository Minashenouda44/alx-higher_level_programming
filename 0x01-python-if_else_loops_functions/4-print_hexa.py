#!/usr/bin/python3

# a program that prints all numbers from 0 to 98
# in decimal and in hexadecimal

for num in range(99):
    print("{:d} = 0x{:x}" .format(num, num))
