#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print("0")
    else:
        result = sum(map(int, arguments))
        print(result)
