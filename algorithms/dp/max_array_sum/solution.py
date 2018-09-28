#!/usr/bin/env python3
"""
Max Array Sum

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/max-array-sum/problem
"""

from typing import List


def max_array_sum(arr: List[int]) -> int:
    """
    Return the maximum sum of an array subset of non-adjacent items.

    :time: O(n)
    :space: O(n)
    """
    max_sum = [0] * (len(arr) + 2)
    for i, num in enumerate(arr, start=2):
        max_sum[i] = max(max_sum[i - 2] + num, max_sum[i - 1])
    return max_sum[-1]


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    max_sum = max_array_sum(arr)
    print(max_sum)


if __name__ == '__main__':
    main()
