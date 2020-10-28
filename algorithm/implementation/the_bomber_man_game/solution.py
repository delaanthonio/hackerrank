#!/usr/bin/env pypy3
"""
The Bomberman Game


:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/bomber-man
"""

import sys

def stringify(cell: int):
    if cell == 0:
        return '.'
    return 'O'

def numberize(cell: str):
    if cell == 'O':
        return 1
    return 0

def print_grid(grid) -> int:
    for r in grid:
        print(r, file=sys.stderr)
    print(file=sys.stderr)

def print_final_grid(grid) -> int:
    for row in grid:
        final_row = [stringify(x) for x in row]
        print("".join(final_row))

def iterate_grid(grid, wait=False):
    new_grid = []
    for row in grid:
        if wait:
            new_grid.append([x + min(1, x) for x in row])
        else:
            new_grid.append([x + 1 for x in row])
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == 3:
                new_grid[r][c] = 0
                if r > 0:
                    new_grid[r - 1][c] = 0
                if r < len(new_grid) - 1:
                    new_grid[r + 1][c] = 0
                if c > 0:
                    new_grid[r][c - 1] = 0
                if c < len(row) - 1:
                    new_grid[r][c + 1] = 0
    return new_grid


def main():
    rows, _, seconds = [int(x) for x in input().split()]
    grid = []
    for _ in range(rows):
        row = input()
        print(row, file=sys.stderr)
        grid.append([numberize(x) for x in row])
    
    wait = True

    if seconds > 2:
        seconds -= 2
        seconds %= 4
        seconds += 2

    for _ in range(seconds):
        grid = iterate_grid(grid, wait)
        wait = not wait

    print_final_grid(grid)

if __name__ == "__main__":
    main()
