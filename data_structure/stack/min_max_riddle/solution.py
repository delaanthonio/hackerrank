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
    acending_numbers = []
    max_for_window = collections.defaultdict(int)

    # Append the zero to flush all the numbers at the end
    numbers.append(0)
    for window_end, number in enumerate(numbers):
        window_start = window_end
        while acending_numbers and number < acending_numbers[-1][0]:
            popped_number, window_start = acending_numbers.pop()
            window = window_end - window_start
            if popped_number > max_for_window[window]:
                max_for_window[window] = popped_number

        acending_numbers.append((number, window_start))

    maximums = collections.deque()
    number_to_add = 0
    for window_end in range(len(numbers) - 1, 0, -1):
        if max_for_window[window_end] > number_to_add:
            number_to_add = max_for_window[window_end]
        maximums.appendleft(number_to_add)

    return maximums


def main():
    _ = int(input())
    numbers = [int(x) for x in input().split()]
    output = min_max(numbers)
    print(*output)


if __name__ == "__main__":
    main()
