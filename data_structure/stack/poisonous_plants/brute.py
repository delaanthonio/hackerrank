#!/usr/bin/env pypy3
"""
Poisonous Plants

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/poisonous-plants
"""

import itertools
import sys
from typing import List


def min_days(pesticides: List[int]) -> int:
    days = 0
    plants = pesticides[:]

    while True:
        len_before = len(plants)
        neighbors = zip(plants, plants[1:])
        plants = plants[:1] + [right for left, right in neighbors if right <= left]
        len_after = len(plants)
        if len_before == len_after:
            break
        days += 1

    return days


def main():
    _ = int(input())
    nums = [int(x) for x in input().split()]
    output = min_days(nums)
    print(output)


if __name__ == "__main__":
    main()
