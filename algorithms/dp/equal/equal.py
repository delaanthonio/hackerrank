#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/equal/problem
"""

import functools

GIVE_AMOUNTS = [5, 2, 1]


@functools.lru_cache(maxsize=128)
def count_ops(val: int, target: int):
    """Count the number of operations to reduce ``val`` to ``target``."""
    if val == target:
        return 0
    dif = abs(val - target)
    for amount in GIVE_AMOUNTS:
        if amount <= dif:
            return (val - target) // amount + count_ops(
                target + (val - target) % amount, target)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        chocolates = [int(x) for x in input().strip().split()]
        min_val = min(chocolates)
        iterations = [0] * (max(GIVE_AMOUNTS) - min(GIVE_AMOUNTS))
        for val in chocolates:
            for i in range(len(iterations)):
                iterations[i] += count_ops(val, min_val - i)
        print(min(iterations))


if __name__ == '__main__':
    main()
