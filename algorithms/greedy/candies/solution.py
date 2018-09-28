#!/bin/python3
"""
Candies

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/candies/problem
"""

from typing import List


def min_candies(n: int, ratings: List[int]) -> int:
    """
    Return the minimum amount of candies to give to students.

    Candies are assigned using the following rules:
    1. Every student gets at least 1 candy
    2. If 2 students are next to each other, the one with the higher rating
    must receive at least one more candy.
    3. The candies given should be minimized.

    :time: O(n) where n is the amount of students
    :space: O(n)
    """
    candies = [1] * n
    for i, (r1, r2) in enumerate(zip(ratings, ratings[1:])):
        if r2 > r1:
            candies[i + 1] = candies[i] + 1

    ratings, candies = ratings[::-1], candies[::-1]

    for i, (r1, r2) in enumerate(zip(ratings, ratings[1:])):
        if r2 > r1 and candies[i + 1] <= candies[i]:
            candies[i + 1] = candies[i] + 1

    return sum(candies)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
    result = min_candies(n, arr)
    print(result)
