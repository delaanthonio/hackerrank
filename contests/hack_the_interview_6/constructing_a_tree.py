#!/usr/bin/env python3
"""
Constructing a Tree

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/
"""

from typing import Iterable, Tuple


def edges(nodes, score) -> Iterable[Tuple[int, int]]:
    """
    Return the edges of the tree with the desires score.

    1. Check if the score is possible.
    2. Determine the highest edge, that I can insert.
    3. Insert the edge with the highest possible score.

    :time: O(n)
    :space: O(n)
    """
    if score < nodes - 1 or score > (nodes ** 2 - nodes) // 2:
        yield -1, -1
        return

    score_left = score
    parent = 1

    for n in range(2, nodes + 1):
        nodes_left = nodes - n
        if score_left - parent >= nodes_left:
            score_left -= parent
            parent += 1
            yield n - 1, n
        else:
            next_score = score_left - nodes_left
            score_left -= next_score
            yield next_score, n


def main():
    tests = int(input())
    for _ in range(tests):
        nodes, score = [int(x) for x in input().split()]
        for src, dest in edges(nodes, score):
            print("{} {}".format(src, dest))


if __name__ == "__main__":
    main()
