#!/usr/bin/env python3
"""
Minimum Average Waiting Time

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/minimum-average-waiting-time
"""

import heapq

from typing import List, Tuple


def min_avg_time(orders: List[Tuple[int, int]]) -> int:
    total_time = 0
    total_waiting_time = 0
    heap = []  # type: List[Tuple[int, int, int]]
    for order_time, cook_time in sorted(orders):
        heapq.heappush(heap, (order_time + cook_time, order_time, cook_time))
    while heap:
        _, order_time, cook_time = heapq.heappop(heap)
        total_time = max(total_time, order_time)
        total_time += cook_time
        total_waiting_time += total_time - order_time
    return total_waiting_time // len(orders)


def main():
    n = int(input())
    orders = []
    for _ in range(n):
        order_time, cook_time = [int(x) for x in input().split()]
        orders.append((order_time, cook_time))
    min_time = min_avg_time(orders)
    print(min_time)


if __name__ == '__main__':
    main()
