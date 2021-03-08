#!/usr/bin/python3
def magic_calculation(a, b):

    add = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                add += a ** b / i
        except:
            add = a + b
            break
    return add
