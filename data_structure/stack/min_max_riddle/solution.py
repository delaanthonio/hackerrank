#!/usr/bin/env pypy3
"""
Min Max Riddle

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/min-max-riddle
"""

import collections
import sys
from typing import Sequence


def min_max(numbers: Sequence[int]) -> Sequence[int]:
    windows = []
    number_for_window = collections.defaultdict(int)
    window_starts = {}
    numbers.append(0)
    for window_end, number in enumerate(numbers):
        window_start = window_end
        while windows and number < windows[-1]:
            popped_num = windows.pop()
            if popped_num not in window_starts:
                continue
            largest_window = window_end - window_starts[popped_num]
            window_start = window_starts[popped_num]
            del window_starts[popped_num]
            if popped_num > number_for_window[largest_window]:
                number_for_window[largest_window] = popped_num

        windows.append(number)
        if number not in window_starts:
            window_starts[number] = window_start

    maximums = collections.deque()
    number_to_add = 0
    for window_end in range(len(numbers) - 1, 0, -1):
        if number_for_window[window_end] > number_to_add:
            number_to_add = number_for_window[window_end]
        maximums.appendleft(number_to_add)

    return maximums


def main():
    _ = int(input())
    numbers = [int(x) for x in input().split()]
    output = min_max(numbers)
    print(*output)


if __name__ == "__main__":
    main()
