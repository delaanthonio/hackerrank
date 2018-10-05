#!/usr/bin/env python
"""
Ice Cream Parlor

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/icecream-parlor
"""

from typing import List, Tuple


def find_indicies(money: int, prices: List[int]) -> Tuple[int, int]:
    price_indices = {}
    for i, price in enumerate(prices, start=1):
        if money - price in price_indices:
            return price_indices[money - price], i
        price_indices[price] = i
    return 0, 0


def main():
    trips = int(input())
    for _ in range(trips):
        money = int(input())
        flavors = int(input())
        prices = [int(x) for x in input().split()]
        indices = find_indicies(money, prices)
        print(*indices)


if __name__ == '__main__':
    main()
