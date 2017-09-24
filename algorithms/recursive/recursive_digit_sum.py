#!/usr/bin/env python3
"""Solution for: https://www.hackerrank.com/challenges/recursive-digit-sum"""


def super_digit(n: int) -> int:
    """Return the result of summing of a number's digits until 1 digit remains."""
    ds = n % 9
    if ds:
        return ds
    return 9


def main():
    """Print the concatenated supoer digit of a number"""
    n, k = [int(x) for x in input().strip().split()]
    print(super_digit(n * k))


if __name__ == '__main__':
    main()
