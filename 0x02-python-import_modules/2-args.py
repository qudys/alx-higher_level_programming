#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length_argv = len(sys.argv)
    if (length_argv == 1):
        print("0 arguments.")
    elif (length_argv == 2):
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif (length_argv > 2):
        print("{} arguments:".format((length_argv) - 1))
        for i in range(1, length_argv):
            print("{}: {}".format(i, sys.argv[i]))
