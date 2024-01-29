#!/usr/bin/python3


import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check the column on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    """
    Recursive utility function to solve N Queens problem
    """
    if col == n:
        # All queens are placed successfully, add the solution to the list
        solution = [[row, col] for row, col in enumerate(board)]
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place the queen

            solve_nqueens_util(board, col + 1, n, solutions)

            board[i][col] = 0  # Backtrack


def solve_nqueens(n):
    """
    Solve the N Queens problem and print the solutions
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
