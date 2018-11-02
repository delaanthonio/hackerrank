#!/usr/bin/env python3
"""Solution for: https://www.hackerrank.com/challenges/common-child"""


def lcs(s1: str, s2: str) -> int:
    """Return the longest common substing of two strings."""
    table = [[0] * (len(s2) + 1) for _ in range(2)]
    for x in s1:
        for j, y in enumerate(s2, start=1):
            if x == y:
                table[1][j] = table[0][j - 1] + 1
            elif table[1][j - 1] > table[0][j]:
                table[1][j] = table[1][j - 1]
            else:
                table[1][j] = table[0][j]
    return table[-1][-1]


def main():
    """Print the length of the longest common substing of two stings"""
    s1 = input().strip()
    s2 = input().strip()
    print(lcs(s1, s2))


if __name__ == '__main__':
    main()
