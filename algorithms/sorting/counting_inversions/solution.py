#!/usr/bin/env python3
"""
:author: Dela Anthonio
:hackerrank: hackerrank.com/delaanthonio
:problem: hackerrank.com/challenges/ctci-merge-sort
"""

from typing import List, Tuple


def merge_sort(arr: List[int]) -> Tuple[List[int], int]:
    """Return ``arr`` sorted and the amount of inversions in ``arr``."""
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, ls = merge_sort(arr[:mid])
    right, rs = merge_sort(arr[mid:])
    swaps = ls + rs
    merged = []
    ri = 0
    for li in range(len(left)):
        while ri < len(right) and right[ri] < left[li]:
            merged.append(right[ri])
            swaps += len(left) - li
            ri += 1
        merged.append(left[li])
    merged.extend(right[ri:])
    return merged, swaps


def main():
    d = int(input())
    for _ in range(d):
        n = int(input())
        arr = [int(x) for x in input().split()]
        _, swaps = merge_sort(arr)
        print(swaps)


if __name__ == '__main__':
    main()
