#!/usr/bin/env python3
"""
Is it T-shaped?

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/codeagon/challenges/is-it-t-shaped
"""

from collections import defaultdict
from typing import List, Tuple


def is_t_shaped(grid: List[Tuple[int, int]]) -> bool:
    xs = defaultdict(set)
    ys = defaultdict(set)
    for x, y in grid:
        xs[x].add(y)
        ys[y].add(x)
    if len(xs) < 3 or len(ys) < 3:
        return False
    for x_val in xs:
        if len(xs[x_val]) == 1:
            t_row = xs[x_val]
            if any(xs[x].isdisjoint(t_row) for x in xs):
                return False
            break
    xs_keys = sorted(xs.keys())
    if any(x2 - x1 > 1 for x1, x2 in zip(xs_keys, xs_keys[1:])):
        return False
    t_center = [x for x in xs if len(xs[x]) == 3][0]
    t_val = list(t_row)[0]
    x_mid = xs_keys[1]
    if t_center == x_mid:
        #        O      OOO
        # Cases: O  and  O
        #       OOO      O
        return xs[t_center] > {t_val - 1, t_val - 2
                               } or xs[t_center] > {t_val + 1, t_val + 2}
    #        O         O
    # Cases: OOO and OOO
    #        O         O
    return xs[t_center] > {t_val + 1, t_val - 1}


def main():
    t = int(input())
    for _ in range(t):
        points = []
        for _ in range(5):
            x, y = [int(x) for x in input().split()]
            points.append((x, y))
        result = is_t_shaped(sorted(points))
        if result:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
