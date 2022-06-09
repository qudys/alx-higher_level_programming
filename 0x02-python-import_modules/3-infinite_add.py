#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    sum = 0
    if (count > 1):
        for i in range(1, count):
            sum += int(sys.argv[i])
        print(sum)
    else:
        print(sum)
