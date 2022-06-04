#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if b > a:
            print("{}{}".format(a, b), end='\n' if a == 8 else ", ")
