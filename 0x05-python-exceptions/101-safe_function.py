#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    final = None
    try:
        final = fct(*args)
    except Exception as error_fct:
        sys.stderr.write("Exception: {}\n".format(error_fct))
    return final
