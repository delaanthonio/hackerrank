#!/usr/bin/env python3
"""
Largest Rectangle

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/largest-rectangle
"""

from typing import Iterable, List


def areas(heights: List[int]) -> Iterable[int]:
    recent = []

    for i, height in enumerate(heights):
        while recent and heights[recent[-1]] >= height:
            h = recent.pop()
            width = i - recent[-1] + 1 if recent else i
            area = width * heights[h]
            yield area
        recent.append(i)

    for w, h in zip(recent, recent[1:]):
        area = (len(heights) - w - 1) * heights[h]
        yield area

    yield len(heights) * heights[recent[0]]


def main():
    n = int(input())
    heights = [int(x) for x in input().split()]
    area = max(areas(heights))
    print(area)


if __name__ == '__main__':
    main()
