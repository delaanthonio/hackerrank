#!/usr/bin/env python3
"""Solution for: https://www.hackerrank.com/challenges/bfsshortreach
"""

import sys
from collections import defaultdict
from queue import Queue
from typing import List

EDGE_LENGTH = 6


def bfs(graph: List[List[int]], start: int) -> List[int]:
    distance = defaultdict(lambda: -1)
    queue = Queue()
    staging = Queue()
    queue.put(start)
    visited = {start}
    rounds = 0
    while queue.qsize():
        while queue.qsize():
            node = queue.get()
            distance[node] = rounds * EDGE_LENGTH
            for n in graph[node]:
                if n not in visited:
                    staging.put(n)
                    visited.add(n)
        queue, staging = staging, queue
        rounds += 1
    out = []
    for i in range(len(graph)):
        out.append(distance[i])
    del out[start]
    return out


def main():
    """Print the """
    queries = int(input())
    for _ in range(queries):
        node_count, edge_count = [int(x) for x in input().split()]
        graph = [[] for _ in range(node_count)]
        for _ in range(edge_count):
            n1, n2 = [int(x) - 1 for x in input().split()]
            graph[n1].append(n2)
            graph[n2].append(n1)
        start = int(input()) - 1
        result = bfs(graph, start)
        print(graph, file=sys.stderr)
        print(*result)


if __name__ == '__main__':
    main()
