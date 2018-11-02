#!/usr/bin/env python3
"""
Greedy Florist

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/greedy-florist
"""

from typing import List


def min_cost(costs: List[int], friend_count: int) -> int:
    total_cost = 0
    purchased = 1
    costs.sort()

    while costs:
        amount = friend_count
        while costs and amount:
            total_cost += costs.pop() * purchased
            amount -= 1
        purchased += 1

    return total_cost


def main():
    flower_count, friend_count = [int(x) for x in input().split()]
    costs = [int(x) for x in input().split()]
    total_cost = min_cost(costs, friend_count)
    print(total_cost)


if __name__ == '__main__':
    main()
