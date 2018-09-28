#!/usr/bin/env python3
"""
:author: Dela Anthonio
:hackerrank: hackerrank.com/delaanthonio
:problem: hackerrank.com/challenges/ctci-bubble-sort
"""

from typing import List


def bubble_sort(arr: List[int]) -> int:
    """Bubble sort a list inplace and return the amount of swaps."""
    swaps = 0
    for _ in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
    return swaps


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    swaps = bubble_sort(arr)
    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(arr[0]))
    print("Last Element: {}".format(arr[-1]))


if __name__ == '__main__':
    main()
