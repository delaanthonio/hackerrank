#!/usr/bin/env python3
"""
Print Function

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/python-print
"""


def main():
    n = int(input())
    nums = range(1, n + 1)
    print(*nums, sep="")


if __name__ == '__main__':
    main()
