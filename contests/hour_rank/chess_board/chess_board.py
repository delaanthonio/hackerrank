#!/usr/bin/env python3
""":problem: https://www.hackerrank.com/contests/hourrank-29/challenges/customized-chess-board"""

from typing import List


def valid_board(board: List[List[int]]) -> bool:
    """Calculate if the board is valid."""
    for row in board:
        if any(x == y for x, y in zip(row, row[1:])):
            return False
    for col in zip(*board):
        if any(x == y for x, y in zip(col, col[1:])):
            return False
    return True


def main():
    """Print whether a board is valid."""
    t = int(input())
    for _ in range(t):
        rows = int(input())
        board = []
        for _ in range(rows):
            row = [int(x) for x in input().strip().split()]
            board.append(row)
        result = valid_board(board)
        if result:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
