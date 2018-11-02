#!/usr/bin/env python3
"""
Davis' Staircase

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/ctci-recursive-staircase
"""

from functools import lru_cache


@lru_cache()
def count_ways(stairs) -> int:
    if stairs < 0:
        return 0
    if stairs <= 1:
        return 1
    return sum(count_ways(stairs - steps) for steps in range(1, 4))


def main():
    n = int(input())
    for _ in range(n):
        stairs = int(input())
        ways = count_ways(stairs)
        print(ways)


if __name__ == '__main__':
    main()
