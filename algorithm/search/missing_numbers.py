#!/usr/bin/env python
"""Problem: https://www.hackerrank.com/challenges/missing-numbers/problem"""

from collections import Counter


def main():
    n = int(input())
    n_counts = Counter(int(x) for x in input().split())
    m = int(input())
    m_counts = Counter(int(x) for x in input().split())
    missing_keys = []

    for key, val in m_counts.items():
        if val != n_counts[key]:
            missing_keys.append(key)

    print(*sorted(missing_keys))


if __name__ == '__main__':
    main()
