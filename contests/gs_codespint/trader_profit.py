#!/usr/bin/env python3
"""Solution for: https://www.hackerrank.com/contests/gs-codesprint/challenges/trader-profit"""

from typing import List


def trader_profit(transactions: int,
                  prices: List[int],
                  buy_price: int=0,
                  profit: int=0) -> int:
    """Calculate the maximum amount of profit that can be made."""
    if (not transactions and not buy_price) or not prices:
        return profit
    if not buy_price:
        return max(
            trader_profit(
                transactions - 1,
                prices[1:],
                buy_price=prices[0],
                profit=profit),
            trader_profit(transactions, prices[1:], profit=profit))
    # Check to sell stock
    if prices[0] > buy_price:
        return max(
            trader_profit(
                transactions,
                prices[1:],
                buy_price=0,
                profit=profit + prices[0] - buy_price),
            trader_profit(
                transactions, prices[1:], buy_price=buy_price, profit=profit))
    # Couldn't sell product
    return trader_profit(
        transactions, prices[1:], buy_price=buy_price, profit=profit)


def main():
    """Print the maximum profit for each query."""
    query_count = int(input())
    for _ in range(query_count):
        max_transactions = int(input())
        input()
        stock_prices = [int(x) for x in input().split()]
        result = trader_profit(max_transactions, stock_prices)
        print(result)


if __name__ == '__main__':
    main()
