#!/usr/bin/python3
def uppercase(str):
    for count in range(len(str)):
        upchar = str[count]
        if (ord(upchar) >= 97 and ord(upchar) < 123):
            upchar = chr(ord(upchar) - 32)
        print("{}".format(upchar), end='')
    print()
