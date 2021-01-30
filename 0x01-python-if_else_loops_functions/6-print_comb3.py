#!/usr/bin/python3
for number in range(0, 100):
    units = number % 10
    tens = number / 10
    if (number == 89):
        print("{}".format(number))
    elif (units != tens and units > tens):
        print("{:02d}, ".format(number), end="")
