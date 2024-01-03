#!/usr/bin/python3
import string
letters = []
for i in range (len (string.ascii_lowercase) - 1, -1, -1):
    if i % 2 == 0:
        letters.append (string.ascii_lowercase [i].upper ())
    else:
        letters.append (string.ascii_lowercase [i])
        result = "".join (letters)
        print ("{}".format (result))
