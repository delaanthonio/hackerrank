#!/usr/bin/env python3
"""
Special Palindrome Again

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://hackerrank.com/challenges/special-palindrome-again
"""


def count_palindromes(string: str) -> int:
    clusters = []
    palidromes = 0
    last_char = string[0]
    repeats = 0

    for char in string + "\0":
        if char == last_char:
            repeats += 1
        else:
            palidromes += (repeats * repeats + repeats) // 2
            clusters.append((last_char, repeats))
            last_char = char
            repeats = 1

    for prev, cur, next in zip(clusters, clusters[1:], clusters[2:]):
        if cur[1] == 1 and prev[0] == next[0]:
            palidromes += min(prev[1], next[1])

    return palidromes


def main():
    n = int(input())
    string = input()
    result = count_palindromes(string)
    print(result)


if __name__ == '__main__':
    main()
