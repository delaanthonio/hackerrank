#!/usr/bin/env python3
"""
Alternating Characters

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://hackerrank.com/challenges/alternating-characters
"""


def min_deletions(chars: str) -> int:
    """
    Return the amount of letters to delete in ``chars``.

    Delete all adjacent characters to create an alternating string.

    :time: O(n)
    :space: O(1)
    """
    deletions = 0
    prev_char, *chars = chars
    for c in chars:
        if prev_char == c:
            deletions += 1
        prev_char = c
    return deletions


def main():
    n = int(input())
    for _ in range(n):
        chars = input()
        print(min_deletions(chars))


if __name__ == '__main__':
    main()
