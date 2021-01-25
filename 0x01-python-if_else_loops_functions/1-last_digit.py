#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastdig = number % 10
else:
    lastdig = (number * -1) % 10
if lastdig > 5:
    print('Last digit of {:d} is {:d} and is greater than 5'.format(number,lastdig))
elif lastdig == 0:
    print('Last digit of {:d} is {:d} and is 0'.format(number,lastdig))
else:
    print('Last digit of {:d} is {:d} and is less than 6 and not 0'.format(number,lastdig))
