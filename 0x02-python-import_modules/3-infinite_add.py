#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argum = sys.argv
    size = len(argum) - 1
    accum = 0
    for ind in range(1, size + 1):
        accum = accum + int(argum[ind])
    print("{}".format(accum))
