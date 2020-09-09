#!/usr/bin/env python3
"""
Solving for Queries with Cups

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/hack-the-interview-vi/challenges/the-cup-game
"""

from bisect import bisect_left, bisect_right
from collections import defaultdict


def main():
    _, _, swaps, queries = (int(x) for x in input().split())
    cups = defaultdict(bool)
    for ball in (int(x) for x in input().split()):
        cups[ball] = True

    for _ in range(swaps):
        l, r = (int(x) for x in input().split())
        cups[l], cups[r] = cups[r], cups[l]

    cups_with_balls = sorted(cup for cup, has_ball in cups.items() if has_ball)

    for _ in range(queries):
        l, r = (int(x) for x in input().split())
        left_cup = bisect_left(cups_with_balls, l)
        right_cup = bisect_right(cups_with_balls, r)
        print(right_cup - left_cup, end=" ")


if __name__ == "__main__":
    main()
