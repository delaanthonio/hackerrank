#!/usr/bin/env python
"""Problem: https://www.hackerrank.com/challenges/icecream-parlor/problem"""


def main():
    trips = int(input())
    for _ in range(trips):
        dollars = int(input())
        flavors = int(input())
        prices = [int(x) for x in input().split()]
        price_table = {}
        for i, price in enumerate(prices, start=1):
            if dollars - price in price_table:
                print(*sorted([i, price_table[dollars - price]]))
                break
            price_table[price] = i


if __name__ == '__main__':
    main()
