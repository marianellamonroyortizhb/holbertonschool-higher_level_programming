#!/usr/bin/python3
def remove_char_at(str, n):
    if (n >= 0):
        slice_str = str[:n] + str[n + 1:]
        return (slice_str)
    else:
        return (str)
