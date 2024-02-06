#!/usr/bin/python3
""" appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ open the file with the specified file name """

    with open(filename, mode='a', encoding='utf-8') as file:
        """ write the text to the file """

        file.write(text)
        """ return the number of characters written """

        return len(text)
