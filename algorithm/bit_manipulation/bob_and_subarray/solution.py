#!/usr/bin/env python3
"""
Bob and Subarray

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/codeagon/challenges/bob-and-subarray-or
"""

from typing import List
import sys


def subarray_or_sum(arr: List[int]) -> int:
    s = 0
    vals = []
    for x in arr:
        for i, val in enumerate(vals):
            vals[i] |= x
        vals.append(x)
        s += sum(vals)
    return s


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    result = subarray_or_sum(arr)
    print(result)


if __name__ == '__main__':
    main()
