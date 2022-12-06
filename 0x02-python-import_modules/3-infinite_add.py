#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_list = sys.argv[1:]
    res = 0

    for argv in argv_list:
        res += int(argv)
    print("{}".format(res))
