#!/usr/bin/env pypy3
"""
ginortS

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/pythonist3/challenges/ginorts
"""

import sys


def main():
    word = input()
    lower_case = sorted(filter(lambda x: x.islower(), word))
    upper_case = sorted(filter(lambda x: x.isupper(), word))
    odd_digits = sorted(filter(lambda x: x.isdigit() and int(x) % 2 == 1, word))
    even_digits = sorted(filter(lambda x: x.isdigit() and int(x) % 2 == 0, word))
    print("".join(lower_case + upper_case + odd_digits + even_digits))


if __name__ == "__main__":
    main()
