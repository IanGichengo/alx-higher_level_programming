#!/usr/bin/python3
""" appends a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ open the file in read and write mode """

    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
