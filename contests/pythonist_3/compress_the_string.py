#!/usr/bin/env pypy3
"""
Compress the String!

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/pythonist3/challenges/compress-the-string
"""

import itertools
import sys


def main():
    word = input()
    for num, group in itertools.groupby(word):
        output = len(list(group)), int(num)
        print(output, end=' ')


if __name__ == "__main__":
    main()
