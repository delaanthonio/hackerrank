#!/usr/bin/env python3
"""
Solution for https://www.hackerrank.com/challenges/coin-change/problem
"""

from typing import List


def count_ways(target: int, coins: List[int]) -> int:
    """
    Count the number of ways we can count to ``target`` with values ``coins``.

    :param target: The target value.
    :param coins: The coins we can use to reach target.
    :returns: The amount of ways we can count to target using coins.
    """
    cols = target + 1
    rows = len(coins) + 1
    table = [[0] * cols for _ in range(rows)]
    for row in range(1, rows):
        coin = coins[row - 1]
        for col in range(1, cols):
            if coin > col:
                table[row][col] = table[row - 1][col]
            elif coin == col:
                table[row][col] = table[row - 1][col] + 1
            else:
                table[row][col] = table[row - 1][col] + table[row][col - coin]
    return table[-1][-1]


def main():
    m, n = [int(x) for x in input().strip().split()]
    coins = sorted({int(x) for x in input().strip().split()})
    print(count_ways(m, coins))


if __name__ == '__main__':
    main()
