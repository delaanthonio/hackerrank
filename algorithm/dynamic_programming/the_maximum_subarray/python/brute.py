#!/usr/bin/env pypy3
"""
The Maximum Subarray

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/maxsubarray
"""

from typing import Tuple, List
import functools
import sys


def max_subarray(arr: List[int]) -> Tuple[int, int]:
    """
    :time: O(n)
    :space: O(n)
    """
    max_val = max(x for x in arr)
    if max_val < 0:
        return max_val, max_val
    max_subsequence = sum(x for x in arr if x > 0)
    max_subarray = 0
    current_sum = 0

    for x in arr:
        current_sum += x
        if current_sum < 0:
            current_sum = 0
        max_subarray = max(max_subarray, current_sum)

    return max_subarray, max_subsequence


def main():
    tests = int(input())
    for _ in range(tests):
        input()
        arr = [int(x) for x in input().split()]
        array_sum, sequence_sum = max_subarray(arr)
        print(array_sum, sequence_sum)


if __name__ == "__main__":
    main()
