#!/bin/python3
"""
Sherlock and the Valid String

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/sherlock-and-valid-string
"""


from collections import defaultdict


def is_valid_string(string: str) -> bool:
    """Determine if a string is valid."""

    if not string:
        return False

    characters = defaultdict(int)

    for char in string:
        characters[char] += 1

    counts = defaultdict(int)

    for value in characters.values():
        counts[value] += 1

    if len(counts) == 1:
        return True

    if len(counts) == 2:
        return 1 in counts.values()

    return False


def main():
    """Determine if strings are valid."""
    string = input().strip()
    result = is_valid_string(string)
    if result:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
