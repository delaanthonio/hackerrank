#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/crush/problem
"""


def main():
    n, m = [int(x) for x in input().split()]
    arr = [0] * (n + 1)
    for _ in range(m):
        l, r, val = [int(x) for x in input().split()]
        arr[l - 1] += val
        arr[r] -= val
    max_val = 0
    cur = 0
    for val in arr:
        cur += val
        if cur > max_val:
            max_val = cur
    print(max_val)


if __name__ == '__main__':
    main()
