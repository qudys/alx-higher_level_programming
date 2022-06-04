#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) > 96:
            str[i] -= 32
        print("{}".format(str[i]), end="" if i != len(str) - 1 else "\n")
