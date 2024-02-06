#!/usr/bin/python3
""" writes a string to a text file """


def write_file(filename="", text=""):
    """ opens the file with the specified filename """

    with open(filename, mode='w', encoding='utf-8') as file:
        """ write the text to the file """
        file.write(text)
        """ return the number of characters written """
        return len(text)
