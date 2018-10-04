#!/usr/bin/env python3
"""
Luck Balance

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/luck-balance
"""

import sys

from typing import List, Tuple


def luck_balance(contests: List[Tuple[int, int]], important) -> int:
    important_contests = sorted((l for l, i in contests if i), reverse=True)
    luck = 0
    luck += sum(important_contests[:important])
    luck -= sum(important_contests[important:])
    luck += sum(l for l, i in contests if not i)
    return luck


def main():
    _, important = [int(x) for x in input().split()]
    contests = [tuple(int(x) for x in line.split()) for line in sys.stdin]
    luck = luck_balance(contests, important)
    print(luck)


if __name__ == '__main__':
    main()
