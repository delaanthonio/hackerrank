#!/usr/bin/env python3
"""
Max Min

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/angry-children
"""

import sys
from typing import List


def max_min(k: int, arr: List[int]) -> int:
    arr.sort()
    return min(x - y for x, y in zip(arr[k - 1:], arr))


def main():
    n = int(input())
    k = int(input())
    arr = [int(x) for x in sys.stdin]
    result = max_min(k, arr)
    print(result)


if __name__ == '__main__':
    main()
