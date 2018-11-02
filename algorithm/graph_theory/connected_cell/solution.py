#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
"""

from typing import List, Set, Tuple

Cell = Tuple[int, int]


def dfs_region(grid: List[List[int]], visited: Set[Cell], start: Cell) -> int:
    area = 0
    if start in visited:
        return 1
    cells = [start]
    while cells:
        cell = cells.pop()
        row = cell[0]
        col = cell[1]
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if grid[i][j] and (i, j) not in visited:
                    cells.append((i, j))
                    visited.add((i, j))
                    area += 1

    return area


def main():
    rows = int(input())
    cols = int(input())
    grid = []
    grid.append([0] * (cols + 2))
    for _ in range(rows):
        grid.append([0] + [int(x) for x in input().split()] + [0])
    grid.append([0] * (cols + 2))
    max_area = 0
    visited = set()
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if grid[i][j]:
                cell = (i, j)
                area = dfs_region(grid, visited, cell)
                if area > max_area:
                    max_area = area

    print(max_area)


if __name__ == '__main__':
    main()
