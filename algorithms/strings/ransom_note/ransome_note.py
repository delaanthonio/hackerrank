#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""

from collections import Counter


def main():
    m, n = [int(x) for x in input().split()]
    magazine = Counter(x for x in input().split())
    note = Counter(x for x in input().split())
    if all(note[word] <= magazine[word] for word in note):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
