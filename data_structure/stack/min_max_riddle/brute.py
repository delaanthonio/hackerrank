#!/usr/bin/env pypy3
"""
Min Max Riddle

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/min-max-riddle
"""

import itertools
import sys
from typing import List


def min_max(nums: List[int]) -> List[int]:
    maximums = []
    window_size = 1
    while window_size <= len(nums):
        windows = []
        for i in range(len(nums) - window_size + 1):
            windows.append(min(itertools.islice(nums, i, i + window_size)))
        maximums.append(max(windows))
        window_size += 1
    return maximums


def main():
    _ = int(input())
    nums = [int(x) for x in input().split()]
    output = min_max(nums)
    print(*output)


if __name__ == "__main__":
    main()
