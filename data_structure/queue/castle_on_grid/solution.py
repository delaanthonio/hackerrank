#!/usr/bin/env python3
"""
Castle on the Grid

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/castle-on-the-grid
"""

import itertools as it
from collections import deque
from typing import Iterable, List, Tuple

Cell = Tuple[int, int]


def take_cells(cells: str, start: int) -> Iterable[int]:
    def is_clear(c: int) -> bool:
        return 0 <= c < len(cells) and cells[c] == '.'

    yield from it.takewhile(is_clear, it.count(start - 1, -1))
    yield from it.takewhile(is_clear, it.count(start + 1))


def castle_moves(rows: List[str], start: Cell, goal: Cell) -> int:
    moves_to = {start: 0}
    cols = list(zip(*rows))
    cells = deque([start])

    def unseen(cell: Cell):
        return cell not in moves_to

    while cells:
        cell = cells.popleft()

        if cell == goal:
            return moves_to[goal]

        x, y = cell

        adjacent_cells = it.chain(
            zip(it.repeat(x), take_cells(rows[x], y)),
            zip(take_cells(cols[y], x), it.repeat(y)))

        for c in filter(unseen, adjacent_cells):
            cells.append(c)
            moves_to[c] = moves_to[cell] + 1

    return -1


def main():
    n = int(input())
    grid = [input() for _ in range(n)]

    start_x, start_y, goal_x, goal_y = [int(x) for x in input().split()]
    start = start_x, start_y
    goal = goal_x, goal_y
    moves = castle_moves(grid, start, goal)
    print(moves)


if __name__ == '__main__':
    main()
