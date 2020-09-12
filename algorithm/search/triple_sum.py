#!/usr/bin/env python3
"""
Triple sum

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/triple-sum/problem
"""

from bisect import bisect
from typing import List, Set


def triplets(arr_a: List[int], arr_b: Set[int], arr_c: List[int]) -> int:
    count = 0
    for b in arr_b:
        count_a = bisect(arr_a, b)
        count_c = bisect(arr_c, b)
        count += count_a * count_c
    return count


def main():
    _ = input()
    arr_a = sorted({int(x) for x in input().split()})
    arr_b = {int(x) for x in input().split()}
    arr_c = sorted({int(x) for x in input().split()})
    count = triplets(arr_a, arr_b, arr_c)
    print(count)


if __name__ == "__main__":
    main()
