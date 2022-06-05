#!/usr/bin/python3
def to_upper(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return ord(c) - 32
    else:
        return ord(c)


def uppercase(str):
    string_copy = ''
    for a in str:
        string_copy += '%c' % to_upper(a)
    print("{}".format(string_copy))
