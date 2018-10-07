#!/usr/bin/env python3
"""
Lonely Integer

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/lonely-integer
"""

from functools import reduce
from operator import xor
from typing import List


def unique_num(nums: List[int]) -> int:
    return reduce(xor, nums)


def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    num = unique_num(nums)
    print(num)


if __name__ == '__main__':
    main()
