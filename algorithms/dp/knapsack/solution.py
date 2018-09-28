#!/usr/bin/env python3
"""
Knapsack

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/unbounded-knapsack/problem
"""

from typing import List


def knapsack(amount: int, weights: List[int]) -> int:
    """
    Return the closet sum to ``amount`` given ``weights``.

    :time: O(m * n)  where m is the amount of weights and n is the amount
    :space: O(n) where n i the amount
    """
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
