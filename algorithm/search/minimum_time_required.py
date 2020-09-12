#!/usr/bin/env python3
"""
Minimum Time Required


:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/minimum-time-required
"""

import sys
from typing import List


def minimum_time(goal: int, machines: List[int], left: int, right: int) -> int:
    if left == right:
        return right
    mid = (left + right) // 2
    mid_sum = sum(mid // x for x in machines)
    print(left,mid, right, mid_sum, file=sys.stderr)
    if mid_sum >= goal:
        return minimum_time(goal, machines, left, mid)
    return minimum_time(goal, machines, mid + 1, right)


def main():
    _, goal = (int(x) for x in input().split())
    machines = sorted(int(x) for x in input().split())
    time = minimum_time(goal, machines, 1, goal * machines[0])
    print(time)


if __name__ == "__main__":
    main()
