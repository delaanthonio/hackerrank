#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
"""


def main():
    n = int(input())
    arr = sorted(int(x) for x in input().split())
    min_abs_diff = min(x - y for x, y in zip(arr[1:], arr))
    print(min_abs_diff)


if __name__ == '__main__':
    main()
