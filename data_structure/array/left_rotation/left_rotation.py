#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/array-left-rotation/problem
"""


def main():
    n, amount = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    result = arr[amount:] + arr[:amount]
    print(*result)


if __name__ == '__main__':
    main()
