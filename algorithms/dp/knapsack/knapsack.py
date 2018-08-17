#!/usr/bin/env python3

from typing import List
"""
Solution for https://www.hackerrank.com/challenges/unbounded-knapsack/problem
"""


def knapsack(amount: int, weights: List[int]) -> int:
    """Calculate the closet sum to ``amount`` given ``weights``."""
    sums = [0] * (amount + 1)
    for weight in weights:
        for val in range(weight, amount + 1):
            sums[val] = max(sums[val], sums[val - weight] + weight)
    return sums[-1]


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().strip().split()]
        weights = sorted({int(x) for x in input().strip().split()})
        print(knapsack(k, weights))


if __name__ == '__main__':
    main()
