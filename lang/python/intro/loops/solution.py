#!/usr/bin/env python3
"""
Loops

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/python-loops
"""


def main():
    n = int(input())
    for x in (x * x for x in range(n)):
        print(x)


if __name__ == '__main__':
    main()
