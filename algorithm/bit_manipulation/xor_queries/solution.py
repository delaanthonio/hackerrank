#!/usr/bin/env python3
"""
Xor Queries

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/codeagon/challenges/xor-queries
"""

import sys


def solve(x: int, l: int, r: int) -> int:
    complement = ~x
    mask = 1
    while mask < r:
        mask *= 2
        mask += 1
    val = complement & mask
    print((val, x, mask), file=sys.stderr)
    if val < l:
        val = l
    elif val > r:
        return max(i ^ x for i in range(mask >> 1, r + 1))
    print((val, x, mask), file=sys.stderr)

    return val ^ x


def main():
    q = int(input())
    for _ in range(q):
        x, l, r = [int(x) for x in input().split()]
        result = solve(x, l, r)
        print(result)


if __name__ == '__main__':
    main()
