#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, num in enumerate(row):
            if idx == len(row) - 1:
                print("{:d}".format(num))
            else:
                print("{:d} ".format(num), end="")
    if not matrix:
        print("$")
