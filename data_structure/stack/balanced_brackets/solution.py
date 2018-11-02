#!/usr/bin/env python3
"""
Balanced Brackets

:author: Dela Anthonio
:hackerrank: hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/balanced-brackets
"""

openning = {"{", "(", "["}
closing = {"}": "{", "]": "[", ")": "("}


def is_balanced(brackets: str) -> str:
    """
    Return whether ``brackets`` is balanced.

    :time: O(n)
    :space: O(n)
    """
    unmatched = []
    for b in brackets:
        if b in openning:
            unmatched.append(b)
        elif not unmatched or closing[b] != unmatched.pop():
            return "NO"
    return "NO" if unmatched else "YES"


def main():
    n = int(input())
    for _ in range(n):
        backets = input()
        result = is_balanced(backets)
        print(result)


if __name__ == '__main__':
    main()
