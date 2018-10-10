#!/usr/bin/env python3
"""
Python If-Else

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/py-if-else
"""


def is_weird(n: int) -> bool:
    weird = False
    if n % 2 == 1 or 6 <= n <= 20:
        weird = True
    return weird


def main():
    n = int(input())
    print("Weird" if is_weird(n) else "Not Weird")


if __name__ == '__main__':
    main()
