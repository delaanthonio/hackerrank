#!/usr/bin/env pypy3
"""
Poisonous Plants

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/poisonous-plants
"""

import itertools
import sys
from collections import namedtuple
from typing import List

Plant = namedtuple('Plant', 'pesticide days_alive')


def min_days(pesticides: List[int]) -> int:
    days = 0
    plants = []
    min_pesticide = pesticides[0]
    for pesticide in pesticides:
        if pesticide <= min_pesticide:
            min_pesticide = pesticide
            plants.append(Plant(pesticide, 0))
            continue
        elif not plants or pesticide <= plants[-1].pesticide:
            days_alive = plants[-1].days_alive + 1
            while pesticide <= plants[-1].pesticide:
                days_alive = max(plants[-1].days_alive + 1, days_alive)
                plants.pop()
            plants.append(Plant(pesticide, days_alive)) 
        else:
           plants.append(Plant(pesticide, 1)) 
    days = max(days for pesticide, days in plants)
    return days

                                               
def main():
    _ = int(input())
    nums = [int(x) for x in input().split()]
    output = min_days(nums)
    print(output)


if __name__ == "__main__":
    main()
