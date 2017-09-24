#!/usr/bin/env python3
"""Solution for: https://www.hackerrank.com/contests/gs-codesprint/challenges/buy-maximum-stocks"""

from collections import namedtuple
from typing import List

Stock = namedtuple('Stock', ['price', 'count'])


def buy_max_stocks(dollars: int, stock_prices: List[int]) -> int:
    """Calculate ..."""
    max_stocks = 0
    stocks = []
    for i, stock_price in enumerate(stock_prices, start=1):
        stocks.append(Stock(stock_price, i))
    sorted_stocks = sorted(stocks, key=lambda x: x.price)
    for stock in sorted_stocks:
        if stock.price > dollars:
            break
        stock_amount = min(dollars // stock.price, stock.count)
        max_stocks += stock_amount
        dollars -= stock.price * stock_amount
    return max_stocks


def main():
    """Print ..."""
    input()
    stock_prices = [int(x) for x in input().split()]
    dollars = int(input())
    result = buy_max_stocks(dollars, stock_prices)
    print(result)


if __name__ == '__main__':
    main()
