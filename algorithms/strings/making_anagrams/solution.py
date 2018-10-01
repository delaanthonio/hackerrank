#!/usr/bin/env python3
"""
Strings: Making Anagrams

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/ctci-making-anagrams
"""

from collections import defaultdict


def make_anagram(a: str, b: str) -> int:
    counts = defaultdict(int)
    for char in a:
        counts[char] += 1
    for char in b:
        counts[char] -= 1
    return sum(abs(x) for x in counts.values())


def main():
    a = input()
    b = input()
    result = make_anagram(a, b)
    print(result)


if __name__ == '__main__':
    main()
