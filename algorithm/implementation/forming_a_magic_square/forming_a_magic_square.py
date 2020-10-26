#!/usr/bin/env python3
""" 
Forming a Magic Square 

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/magic-square-forming
"""

from typing import List

magic_squares = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]


def magic_square(square: List[List[int]]) -> int:
    def conversion_cost(src: List[List[int]], tgt: List[List[int]]):
        cost = 0
        for src_row, tgt_row in zip(src, tgt):
            cost += sum(abs(src_col - tgt_col)
                        for src_col, tgt_col in zip(src_row, tgt_row))
        return cost

    return min(conversion_cost(square, msqr) for msqr in magic_squares)


def main():
    square = []
    for _ in range(3):
        square.append([int(x) for x in input().split()])
    cost = magic_square(square)
    print(cost)


if __name__ == '__main__':
    main()
