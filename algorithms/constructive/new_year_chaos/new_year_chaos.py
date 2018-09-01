#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/new-year-chaos/problem
"""

from typing import List


def min_bribes(queue: List[int]) -> int:
    bribes = 0
    if any(val - i > 2 for i, val in enumerate(queue, start=1)):
        return -1
    for i, val in enumerate(queue[1:], start=1):
        j = i
        prev_val = queue[j - 1]
        while j and val < prev_val:
            queue[j], queue[j - 1] = prev_val, val
            bribes += 1
            j -= 1
            prev_val = queue[j - 1]
    return bribes


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        queue = [int(x) for x in input().split()]
        result = min_bribes(queue)
        if result == -1:
            print("Too chaotic")
        else:
            print(result)


if __name__ == '__main__':
    main()
