#!/usr/bin/env pypy3
"""
Abbreviation

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/abbr
"""

import sys
from typing import List


def can_transform(source: str, target: str) -> bool:
    row_count = len(target) + 1
    col_count = len(source) + 1
    grid = [[False] * col_count for _ in range(row_count)]
    grid[0][0] = True
    # Append dummy value so that we loop through last row
    for row, letter_target in enumerate(target + " "):
        for col, letter_source in enumerate(source):
            if not grid[row][col]:
                continue
            if letter_source.upper() == letter_target:
                grid[row + 1][col + 1] = True
            if letter_source.islower():
                grid[row][col + 1] = True
    return grid[-1][-1]


def main():
    queries = int(input())
    for _ in range(queries):
        source = input()
        target = input()
        print("YES" if can_transform(source, target) else "NO")


if __name__ == "__main__":
    main()
