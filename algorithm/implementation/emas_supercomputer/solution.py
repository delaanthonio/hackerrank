#!/usr/bin/env pypy3
"""
Ema's Supercomputer

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/two-pluses
"""

import copy
import sys


def main():
    height, _ = [int(x) for x in input().split()]
    grid = []

    for _ in range(height):
        grid.append(input())

    max_area = 0
    pluses = []
    
    for r, row in enumerate(grid):
        for c in range(len(row)):
            h = 0
            w = 0
            plus = set()
            while (
                r-h >= 0 
            and grid[r - h][c] == 'G' 
            and r+h < len(grid) 
            and grid[r + h][c] == 'G' 
            and c - w >= 0 
            and grid[r][c - w] == 'G' 
            and c + w < len(grid[0]) 
            and grid[r][c + w] == 'G'
            ):
                plus.add((r - h, c))
                plus.add((r + h, c))
                plus.add((r, c - w))
                plus.add((r, c + w))
                pluses.append(copy.deepcopy(plus))
                w += 1
                h += 1

    for p1 in pluses:
        for p2 in pluses:
            if p1.isdisjoint(p2):
                area = len(p1) * len(p2)
                max_area = max(area, max_area)

    print(max_area)


if __name__ == "__main__":
    main()
