#!/usr/bin/python3

for x in range(10):
    for y in range(10):
        if x != y and x <= y:
            if x == 8 and y == 9:
                print("{:d}{:d}".format(x, y))
            else:
                print("{:d}{:d}".format(x, y), end=", ")
