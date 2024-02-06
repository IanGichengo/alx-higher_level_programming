#!/usr/bin/python3
""" reads the content of a text file and prints to stdout """


def read_file(filename=""):
    """ open the file with the specified filename for reading """

    with open(filename, encoding='utf-8') as file:
        """ read the content of the file and print it to stdout """

        print(file.read(), end='')
