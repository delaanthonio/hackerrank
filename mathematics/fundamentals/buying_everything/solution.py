#!/usr/bin/env python3
"""
Buying Everything

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/buying-everything
"""

from typing import List


def min_minutes(distances: List[int], items: int, travel_cost: int) -> int:
    if len(distances) < items:
        return -1

    recent_costs = sum(distances[:items - 1])
    minutes = distances[0] + distances[items - 1] * (items - 1)
    minutes -= recent_costs
    minutes *= travel_cost

    for old, new in zip(distances, distances[items - 1:]):
        total_minutes = old + (new * (items - 1) - recent_costs) * travel_cost
        if total_minutes < minutes:
            minutes = total_minutes
        recent_costs -= old
        recent_costs += new

    return minutes


def main():
    n, m, k = [int(x) for x in input().split()]
    buildings = [int(x) for x in input().split()]
    distances = [i for i, x in enumerate(buildings) if x]
    minutes = min_minutes(distances, m, k)
    print(minutes)


if __name__ == '__main__':
    main()
