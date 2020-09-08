#!/usr/bin/env python3
"""
Solving for Queries with Cups

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/hack-the-interview-vi/challenges/the-cup-game
"""

from collections import defaultdict


def main():
    cups, _, swaps, queries = [int(x) for x in input().split()]
    balls = [int(x) - 1 for x in input().split()]
    cup_list = [0 for _ in range(cups)]
    for ball in balls:
        cup_list[ball] = 1

    for _ in range(swaps):
        l, r = [int(x) - 1 for x in input().split()]
        cup_list[l], cup_list[r] = cup_list[r], cup_list[l]

    ball_prefix = []
    balls_seen = 0
    for cup in cup_list:
        if cup:
            balls_seen += 1
        ball_prefix.append(balls_seen)

    for _ in range(queries):
        l, r = [int(x) - 1 for x in input().split()]
        print(ball_prefix[r] - ball_prefix[l] + cup_list[l], end=" ")


if __name__ == "__main__":
    main()
