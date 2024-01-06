#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for h in range(len(matrix)):
        for k in range(len(matrix[h])):
            print("{:d}".format(matrix[h][k]), end="")
            if k != (len(matrix[h]) - 1):
                print(" ", end="")
                print("")
