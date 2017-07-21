#!/usr/bin/env python3
"""Solution for: https://www.hackerrank.com/contests/w34/challenges/maximum-gcd-and-sum"""

from math import gcd
from typing import Iterator, List


def isqrt(n: int) -> int:
    """Return the square root of an integer."""
    x = n
    y = (x + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x


def factor(num: int) -> Iterator[int]:
    """>>> factor(30) -> [2, 3, 5, 6, 10, 15, 30]."""
    yield num
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            yield i
            yield num // i


def gcd_sum(arr_a: Iterator[int], arr_b: Iterator[int]) -> int:
    """Calculate max gcd sum.
    Complexity: O(n * sqrt(n)).
    """
    max_gcd = 0

    divs_a = {}  # type: Dict[int, int]
    divs_b = {}  # type: Dict[int, int]
    max_sum = 0
    arr_a = sorted(arr_a, reverse=True)
    arr_b = sorted(arr_b, reverse=True)
    for num_a, num_b in zip(arr_a, arr_b):
        if num_a < max_gcd and num_b < max_gcd:
            return max_sum
        additions_a = (x for x in factor(num_a) if x not in divs_a)
        for i in additions_a:
            if i in divs_b and i > max_gcd:
                max_gcd = i
                max_sum = divs_b[i] + num_a
            divs_a[i] = num_a
        additions_b = (x for x in factor(num_b) if x not in divs_b)
        for i in additions_b:
            if i in divs_a and i > max_gcd:
                max_gcd = i
                max_sum = divs_a[i] + num_b
            divs_b[i] = num_b

    return max_sum


def trivial_max_gcd_sum(arr_a: List[int], arr_b: List[int]) -> int:
    """Calculate max gcd sum.
    Complexity: O(n^2).
    """
    max_gcd = 0
    max_sum = 0

    for num_a in arr_a:
        for num_b in arr_b:
            cur_gdc = gcd(num_a, num_b)
            if cur_gdc > max_gcd:
                max_gcd = cur_gdc
                max_sum = num_a + num_b

    return max_sum


def main():
    """Print the maximum gcd sum of A and B."""
    input()
    arr_a = {int(x) for x in input().split()}
    arr_b = {int(x) for x in input().split()}
    result = gcd_sum(arr_a, arr_b)
    print(result)


if __name__ == '__main__':
    main()
