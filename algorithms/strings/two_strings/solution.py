#!/usr/bin/env python3
"""
Two Strings

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/two-strings/problem
"""


def main():
    t = int(input())
    for _ in range(t):
        s1 = set(char for char in input())
        s2 = set(char for char in input())
        if s1.isdisjoint(s2):
            print("NO")
        else:
            print("YES")


if __name__ == '__main__':
    main()
