#!/usr/bin/env python3
"""
Extra Long Factorials

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/extra-long-factorials
"""


def factorial(n: int) -> int:
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def main():
    n = int(input())
    product = factorial(n)
    print(product)


if __name__ == '__main__':
    main()
