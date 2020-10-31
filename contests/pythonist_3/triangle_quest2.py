#!/usr/bin/env pypy3
"""
Triangle Quest 2

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/pythonist3/challenges/triangle-quest-2
"""

for i in range(1, int(input()) + 1):
    print(((10 ** i - 1) // 9) ** 2)
