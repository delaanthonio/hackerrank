#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
"""

from collections import Counter
from math import factorial


def choices(n: int, k: int):
    return factorial(n) // (factorial(k) * factorial(n - k))


def count_anagrams(string: str) -> int:
    """Calculate the amount of substring anagrams."""
    anagrams = Counter()
    for i in range(0, len(string)):
        for j in range(i + 1, len(string) + 1):
            anagram = string[i:j]
            key = tuple(sorted(anagram))
            anagrams[key] += 1

    return sum(choices(val, 2) for val in anagrams.values() if val > 1)


def main():
    q = int(input())
    for _ in range(q):
        s = input().strip()
        result = count_anagrams(s)
        print(result)


if __name__ == '__main__':
    main()
