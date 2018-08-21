#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/frequency-queries/problem
"""

from typing import List, Tuple
from collections import Counter


def process_queries(queries: List[Tuple[int, int]]) -> List[int]:
    """Execute queries and report whether a value with a given count exists."""
    values = Counter()
    counts = Counter()
    results = []
    for query, val in queries:
        if query == 1:
            counts[values[val]] -= 1
            counts[values[val] + 1] += 1
            values[val] += 1
        elif query == 2:
            if val in values and values[val]:
                counts[values[val]] -= 1
                counts[values[val] - 1] += 1
                values[val] -= 1
        else:
            results.append(int(bool(counts[val])))

    return results


def main():
    q = int(input())
    queries = []
    for _ in range(q):
        query, val = [int(x) for x in input().split()]
        queries.append((query, val))
    results = process_queries(queries)
    print(*results, sep='\n')


if __name__ == '__main__':
    main()
