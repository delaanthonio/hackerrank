#!/usr/bin/env pypy3
"""
Hackerland Radio Transmitters

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/hackerland-radio-transmitters
"""


from typing import List
import bisect
import sys


def min_radios(houses: List[int], range: int) -> int:
    """
    1. Find smallest unconvered home.
    2. Find largest home that can cover smallest home.
    3. Place radio on largest home.
    4. Update homes that are covered.
    """
    sorted_houses = sorted(houses) 

    def bisect_radio(target: int) -> int:
        return bisect.bisect_right(sorted_houses, target + range) - 1
        
    max_house = 0
    max_house_i = -1
    radios = 0
    last_house = sorted_houses[-1]

    while max_house < last_house:
        min_house_i = max_house_i + 1
        min_house = sorted_houses[min_house_i]
        radio_house_i = bisect_radio(min_house) 
        radio_house = sorted_houses[radio_house_i]
        max_house_i = bisect_radio(radio_house)
        max_house = sorted_houses[max_house_i]
        radios += 1
        
    return radios


def main():
    _, range = (int(x) for x in input().split())
    houses = [int(x) for x in input().split()]
    radios = min_radios(houses, range)
    print(radios)


if __name__ == "__main__":
    min_radios([1,5,1,2,4,2,3,3,3,3,4,2,4,4,5,5,1], 1)
    # min_radios([9,5,4,2,6,15,12], 2)
    main()
