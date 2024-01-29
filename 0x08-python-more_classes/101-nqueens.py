#!/usr/bin/python3

""" Import sys module """
import sys

""" Check the number of arguments"""
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

""" Check if N is a positive integer"""
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

""" Check if N is at least 4"""
if N < 4:
    print("N must be at least 4")
    sys.exit(1)


""" Define a function to check if a position is safe"""


def is_safe(board, row, col):
    """ Check the left side of the row """
    for i in range(col):
        if board[row][i] == 1:
            return False
    """ Check the upper left diagonal """
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    """ Check the lower left diagonal """
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    """ Return true if no conflict """
    return True


""" Define a function to solve the problem recursively"""


def solve_nqueens(board, col):
    """ If all queens are placed, print the solution """
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return
    """ Try all rows in the current column"""
    for i in range(N):
        """ Check if the position is safe """
        if is_safe(board, i, col):
            """ Place a queen """
            board[i][col] = 1
            """ Recur for the next column """
            solve_nqueens(board, col + 1)
            """ Remove the queen """
            board[i][col] = 0


"""Create an empty board """
board = [[0 for i in range(N)] for j in range(N)]

""" Call the function to solve the problem """
solve_nqueens(board, 0)
