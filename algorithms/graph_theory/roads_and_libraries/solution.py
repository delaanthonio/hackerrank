#!/usr/bin/env python3
"""
Roads and Libraries

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/torque-and-development
"""

from typing import List
from collections import deque


def min_cost(hacker_land: List[List[int]], lib_cst, road_cst) -> int:
    city_groups = 0
    roads_built = 0
    if lib_cst <= road_cst:
        return lib_cst * len(hacker_land)
    unseen = set(range(len(hacker_land)))
    while unseen:
        city_groups += 1
        start_city = unseen.pop()
        visiting = deque(x for x in hacker_land[start_city] if x in unseen)
        unseen.difference_update(visiting)
        while visiting:
            city = visiting.popleft()
            roads_built += 1
            for neighbor in hacker_land[city]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    visiting.append(neighbor)

    return roads_built * road_cst + city_groups * lib_cst


def main():
    query_count = int(input())
    for _ in range(query_count):
        city_cnt, road_cnt, lib_cst, road_cst = [
            int(x) for x in input().split()
        ]
        hacker_land = [[] for _ in range(city_cnt)]
        for _ in range(road_cnt):
            c1, c2 = [int(x) - 1 for x in input().split()]
            hacker_land[c1].append(c2)
            hacker_land[c2].append(c1)
        result = min_cost(hacker_land, lib_cst, road_cst)
        print(result)


if __name__ == '__main__':
    main()
