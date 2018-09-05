#!/usr/bin/env python3
"""
Fraudulent Activity Notifications

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://hackerrank.com/challenges/fraudulent-activity-notifications
"""

from collections import deque
from typing import List

MAX_VAL = 200


def median(histogram: List[int], count: int) -> int:
    """
    Return the median int of ``histogram`` * 2.

    Handles both cases in which the median is an odd or even number.

    :time: O(n)
    :space: O(1)
    """
    mid = count // 2
    if count % 2:
        mid += 1
    total_freq = 0
    median = None
    for cost, freq in enumerate(histogram):
        total_freq += freq
        if total_freq >= mid and freq:
            if median is not None:
                return median + cost
            median = cost
            if count % 2 or total_freq > mid:
                return median * 2


def notifications(costs: List[int], histogram: List[int], recent) -> int:
    """
    Return the amount of notifications for fraudulent activity.

    A purchase is notified as being fraudulent if it's >= to 2x median cost of
    the purchases stored in ``recent``.

    :param costs: The cost of future items.
    :param histogram: Tracks the frequencies of values in ``recent``.
    :param recent: The cost of the last few items purchased.

    :time: O(n * k) where 'n' is the size of ``costs`` and 'k' is the max cost.
    :space: O(n)
    """
    alerts = 0
    days = len(recent)
    for cost in costs:
        if median(histogram, days) <= cost:
            alerts += 1
        outdated_cost = recent.popleft()
        histogram[outdated_cost] -= 1
        recent.append(cost)
        histogram[cost] += 1
    return alerts


def main():
    n, d = [int(x) for x in input().split()]
    costs = [int(x) for x in input().split()]
    histogram = [0] * (MAX_VAL + 1)
    recent = deque()
    for cost in costs[:d]:
        recent.append(cost)
        histogram[cost] += 1
    alerts = notifications(costs[d:], histogram, recent)
    print(alerts)


if __name__ == '__main__':
    main()
