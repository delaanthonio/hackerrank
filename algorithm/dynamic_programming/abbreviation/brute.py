#!/usr/bin/env pypy3
"""
Abbreviation

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/abbr
"""

import sys


def can_transform(source: str, target: str) -> bool:
    if not target:
        return not source or source.islower()

    if target and not source:
        return False

    if not source:
        return False

    char = source[0]

    if char.isupper():
        if target[0] == char:
            return can_transform(source[1:], target[1:])
        return False

    removed = source.replace(char, "", 1)
    uppercased = source.replace(char, char.upper(), 1)

    return can_transform(removed, target) or can_transform(uppercased, target)


def main():
    queries = int(input())
    for _ in range(queries):
        source = input()
        target = input()
        print("YES" if can_transform(source, target) else "NO")


if __name__ == "__main__":
    main()
