#!/usr/bin/env python3
"""
Roads and Libraries

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/torque-and-development
"""

from collections import deque
from typing import List, Set

Graph = List[Set[int]]


def build_roads(hacker_land: Graph, unseen: Set[int], start: int) -> int:
    new_roads = 0
    adjacent = deque([start])
    while adjacent:
        city = adjacent.popleft()
        for new_city in hacker_land[city] & unseen:
            new_roads += 1
            unseen.remove(new_city)
            adjacent.append(new_city)
    return new_roads


def build_cost(hacker_land: Graph, library_cost: int, road_cost: int) -> int:
    city_groups = 0
    roads = 0
    if library_cost <= road_cost:
        return library_cost * len(hacker_land)
    unseen = set(range(len(hacker_land)))
    while unseen:
        city_groups += 1
        start_city = unseen.pop()
        roads += build_roads(hacker_land, unseen, start_city)
    return roads * road_cost + city_groups * library_cost


def main():
    query_count = int(input())
    for _ in range(query_count):
        cities, roads, library_cost, road_cost = [
            int(x) for x in input().split()
        ]
        hacker_land = [set() for _ in range(cities)]
        for _ in range(roads):
            c1, c2 = [int(x) - 1 for x in input().split()]
            hacker_land[c1].add(c2)
            hacker_land[c2].add(c1)
        result = build_cost(hacker_land, library_cost, road_cost)
        print(result)


if __name__ == '__main__':
    main()
