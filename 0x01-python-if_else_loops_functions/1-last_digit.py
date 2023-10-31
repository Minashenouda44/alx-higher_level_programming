#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

tempNumber = abs(number)
lastDigit = tempNumber % 10

if lastDigit == 0:
    print("Last digit of {} is {:d} and is 0" .format(number, lastDigit))
elif lastDigit > 5:
    print("Last digit of {} is {:d} and is greater than 5" .format(number, lastDigit))
elif lastDigit < 6:
    str = "and is less than 6 and not 0"
    if number > 0:
        print("Last digit of {} is {:d} {}" .format(number, lastDigit, str))
    else:
        print("Last digit of {} is -{:d} {}" .format(number, lastDigit, str))
