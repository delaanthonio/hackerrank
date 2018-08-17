#!/usr/bin/env python3
"""
Solution for https://www.hackerrank.com/challenges/coin-change/problem
"""

from typing import List


def count_ways(amount: int, coins: List[int]) -> int:
    """Return the number of ways we can count to ``amount`` with values ``coins``."""
    ways = [1] + [0] * amount
    for coin in coins:
        for val in range(coin, amount + 1):
            ways[val] += ways[val - coin]
    return ways[-1]


def main():
    m, n = [int(x) for x in input().strip().split()]
    coins = sorted({int(x) for x in input().strip().split()})
    print(count_ways(m, coins))


if __name__ == '__main__':
    main()
