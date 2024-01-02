#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_code = ord(c)
        if ascii_code >= 97 and ascii_code <= 122:
            ascii_code -= 32
            print(chr(ascii_code), end="")
            print()
