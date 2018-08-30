#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/count-triplets-1/problem
"""

from collections import defaultdict
from typing import List


def count_triplets(arr: List[int], ratio: int) -> int:
    doubles = defaultdict(int)
    triplets = defaultdict(int)
    triplet_count = 0
    for n in arr:
        triplet_count += triplets[n]
        next = n * ratio
        triplets[next] += doubles[n]
        doubles[next] += 1
    return triplet_count


def main():
    n, r = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    result = count_triplets(arr, r)
    print(result)


if __name__ == '__main__':
    main()
