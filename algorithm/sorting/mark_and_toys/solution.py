#!/usr/bin/env python3
"""
:author: Dela Anthonio
:hackerrank: hackerrank.com/delaanthonio
:problem: hackerrank.com/challenges/mark-and-toys
"""


def main():
    n, k = [int(x) for x in input().split()]
    candies = 0
    cost = 0
    prices = sorted(int(x) for x in input().split())
    for p in prices:
        cost += p
        if k < cost:
            break
        candies += 1
    print(candies)


if __name__ == '__main__':
    main()
