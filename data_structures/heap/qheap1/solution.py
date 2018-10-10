#!/usr/bin/env python3
"""
QHEAP1

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/qheap1
"""

import heapq


def main():
    queries = int(input())
    heap = []
    valid_items = set()
    for _ in range(queries):
        q = [int(x) for x in input().split()]
        if q[0] == 1:
            heapq.heappush(heap, q[1])
            valid_items.add(q[1])
        elif q[0] == 2:
            valid_items.remove(q[1])
        else:
            while heap[0] not in valid_items:
                heapq.heappop(heap)
            print(heap[0])


if __name__ == '__main__':
    main()
