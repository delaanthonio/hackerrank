#!/usr/bin/env python3
"""
Construct the Array

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/construct-the-array
"""

LIMIT = 10**9 + 7


def count_ways(n: int, k: int, x: int) -> int:
    ways_end_k = [1] * (n - 1)
    ways_end_1 = [0] * (n - 1)
    for i, ways_k, ways_1 in zip(range(1, n - 1), ways_end_k, ways_end_1):
        ways_end_k[i] = (ways_k * (k - 2) + ways_1) % LIMIT
        ways_end_1[i] = ((k - 1) * ways_k) % LIMIT
    if x == 1:
        return ways_end_1[-1]
    return ways_end_k[-1]


def main():
    n, k, x = [int(x) for x in input().split()]
    ways_end_k = count_ways(n, k, x)
    print(ways_end_k)


if __name__ == '__main__':
    main()
