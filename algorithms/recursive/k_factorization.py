#!/usr/bin/env python3
"""Solution for: https://www.hackerrank.com/challenges/k-factorization"""

import sys
from typing import List, Optional, Set


def isqrt(n: int) -> int:
    """Returns the square root of an integer."""
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def factorize(n: int) -> Set[int]:
    """Returns the factors of a number as a set."""
    factors = {n}
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors


def _k_factorize(n: int, factors: List[int],
                 lexical_factors: List[int]) -> Optional[List[int]]:
    if n <= 1:
        return sorted(lexical_factors)
    if not factors:
        return None
    first_factor = factors[0]
    if n % first_factor == 0:
        new_lexical_factors = lexical_factors[:]
        new_lexical_factors.append(first_factor)
        result = _k_factorize(n // first_factor, factors, new_lexical_factors)
        if result:
            return result
    return _k_factorize(n, factors[1:], lexical_factors)


def k_factorize(n: int, factors: List[int]) -> List[int]:
    """Return the result of summing of a number's digits until 1 digit remains."""
    trimmed_factors = []
    lexical_series = [1]
    for f in factors:
        if n % f == 0:
            trimmed_factors.append(f)
    result = _k_factorize(n, sorted(trimmed_factors, reverse=True), [])
    if result:
        total = 1
        for x in result:
            total *= x
            lexical_series.append(total)
        return lexical_series
    return [-1]


def main():
    """Print the concatenated supoer digit of a number."""
    n, _ = [int(x) for x in input().strip().split()]
    factors = [int(x) for x in input().strip().split()]
    print(*k_factorize(n, factors))


if __name__ == '__main__':
    main()
