#!/usr/bin/env python3
"""Solution for: https://www.hackerrank.com/contests/gs-codesprint/challenges/time-series-queries"""

from collections import namedtuple
from typing import List

Query = namedtuple('Query', ['type', 'value'])
Stock = namedtuple('Stock', ['time_stamp', 'price'])


def time_series_queries(stocks: List[Stock], queries: List[Query]) -> List[int]:
    """Return a list of Query results"""
    results = []
    price_sorted_stocks = sorted(stocks, key=lambda x: x.price, reverse=True)
    for query in queries:
        if query.type == 1:
            for stock in stocks:
                if stock.price >= query.value:
                    results.append(stock.time_stamp)
                    break
            else:
                results.append(-1)
        else:
            for stock in price_sorted_stocks:
                if stock.time_stamp >= query.value:
                    results.append(stock.price)
                    break
            else:
                results.append(-1)
    return results


def main():
    """Print the result of queries."""
    std_input = []

    try:
        while True:
            std_input.extend([int(x) for x in input().split()])
    except EOFError:
        pass

    record_count = std_input[0]
    query_count = std_input[1]
    time_stamps = std_input[2:2 + record_count]
    prices = std_input[2 + record_count:2 + 2 * record_count]
    stocks = []
    for time_stamp, stock_price in zip(time_stamps, prices):
        stocks.append(Stock(time_stamp, stock_price))
    queries = []
    base = 2 + 2 * record_count

    for i in range(query_count):
        query_type = std_input[base + 2 * i],
        query_val = std_input[base + 2 * i + 1]
        queries.append(Query(query_type, query_val))
    print(*time_series_queries(stocks, queries), sep='\n')


if __name__ == '__main__':
    main()
