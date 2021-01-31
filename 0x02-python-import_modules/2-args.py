#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argum = sys.argv
    size = len(argum) - 1
    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("1 argument:")
        print("1: {}".format(argum[1]))
    else:
        print("{} arguments:".format(size))
        for ind in range(1, size + 1):
            print("{}: {}".format(ind, argum[ind]))
