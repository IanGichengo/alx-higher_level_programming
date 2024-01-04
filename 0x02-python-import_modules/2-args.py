#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    if num == 0:
        print("0 arguments.")
    else:
        plural = "s" if num > 1 else ""
        print("{} argument{}:".format(num, plural))
        
        for i in range(1, num + 1):
            print("{}: {}".format(i, sys.argv[i]))
