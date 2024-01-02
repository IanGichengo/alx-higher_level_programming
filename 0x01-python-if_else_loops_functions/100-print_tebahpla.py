#!/usr/bin/python3
for i in range(122, 96, -1):
    c = chr(i)
    ascii_code = ord(c)
    if ascii_code % 2 == 0:
        ascii_code -= 32
        c = chr(ascii_code)
        print(c, end="")
