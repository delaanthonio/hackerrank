#!/usr/bin/env python3
"""
Larry's Array

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/larrys-array
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


def can_sort(arr: List[int]) -> bool:
    _, inversions = merge_sort(arr)
    return inversions % 2 == 0


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        if can_sort(arr):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
