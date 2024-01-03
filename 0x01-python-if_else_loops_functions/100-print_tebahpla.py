#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    print(chr(i) + chr(i - ord('A') + ord('a')), end='')
