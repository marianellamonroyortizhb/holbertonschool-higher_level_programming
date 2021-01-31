#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if size != 0:
        return (size, sentence[0])
    else:
        return (0, None)
