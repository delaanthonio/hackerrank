#!/usr/bin/env python3
""":problem: https://www.hackerrank.com/contests/hourrank-29/challenges/array-partition"""

from collections import defaultdict
from typing import Dict, Iterator, List

MOD = 10**9 + 7

MAX_VAL = 10**6


def primes_sieve(limit: int) -> List[int]:
    """Returns all primes under ``limit`` in increasing order."""
    a = [True] * limit
    a[0] = False

    for i, isprime in enumerate(a[1:], start=2):
        if isprime:
            for n in range(i * i, limit + 1, i):
                a[n - 1] = False

    return [i for i, x in enumerate(a, start=1) if x]


def union(parents: Dict[int, int], ranks: Dict[int, int], pid,
          pid2: int) -> None:
    root1 = find(parents, pid)
    root2 = find(parents, pid2)
    if root1 == root2:
        return
    if ranks[root1] >= ranks[root2]:
        greater = root1
        lesser = root2
    else:
        greater = root2
        lesser = root1
    ranks[greater] += ranks[lesser] + 1
    parents[lesser] = parents[greater]


def find(parents: Dict[int, int], key: int) -> int:
    parent = parents[key]
    while not parent == parents[parent]:
        tmp_parent = parents[parent]
        parent = parents[tmp_parent]
    parents[key] = parent
    return parent


def prime_factors(num: int, primes: List[int]) -> Iterator[int]:
    """Yields all prime factors of ``num`` in increasing order."""
    for p in primes:
        if p * p > num:
            break
        if num % p == 0:
            while num % p == 0:
                num //= p
            yield p
    if num > 1:
        yield num


def array_partition(nums: List[int], primes: List[int]) -> int:
    parents = {x: x for x in nums + primes}
    ranks = defaultdict(int)
    for n in nums:
        for p in prime_factors(n, primes):
            union(parents, ranks, n, p)
    components = {find(parents, n) for n in nums}
    paritions = len(components)
    ones = sum(x for x in nums if x == 1)
    if ones >= 2:
        paritions += ones - 1
    return (1 << paritions) % MOD - 2


def main():
    t = int(input())
    primes = primes_sieve(MAX_VAL // 2)
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        result = array_partition(arr, primes)
        print(result)


if __name__ == '__main__':
    main()
