#!/usr/bin/env python3
"""
Sherlock and Cost

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/sherlock-and-cost/problem
"""

from typing import List


def sherlock_and_cost(b: List[int]) -> int:
    a_min = [0] * len(b)  # Store
    a_max = [0] * len(b)
    for i, (prev, cur) in enumerate(zip(b, b[1:]), start=1):
        a_min[i] = a_max[i - 1] + prev - 1
        a_max[i] = max(a_max[i - 1] + prev - cur, a_min[i - 1] + cur - 1)
    return max(a_min[-1], a_max[-1])


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = [int(x) for x in input().strip().split()]
        print(sherlock_and_cost(b))


if __name__ == '__main__':
    main()
