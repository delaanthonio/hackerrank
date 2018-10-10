#!/usr/bin/env python3
"""
Write a function

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/write-a-function
"""


def is_leap_year(year: int) -> int:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main():
    year = int(input())
    print(is_leap_year(year))


if __name__ == '__main__':
    main()
