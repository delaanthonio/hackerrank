#!/usr/bin/env python3
"""
Breadth First Search: Shortest Reach

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://hackerrank.com/challenges/bfsshortreach
"""

from collections import deque
from typing import List

EDGE_LENGTH = 6


def bfs(graph: List[List[int]], start: int) -> List[int]:
    """
    Return the shortest distance from each node in ``graph`` to ``start``.

    :time: O(v) where 'v' is the amount of vertices in ``graph``.
    :space: O(v)
    """
    distances = [-1] * len(graph)
    distances[start] = 0
    nodes = deque([start])
    while nodes:
        node = nodes.popleft()
        for nbr in graph[node]:
            if distances[nbr] == -1:
                distances[nbr] = distances[node] + EDGE_LENGTH
                nodes.append(nbr)
    del distances[start]
    return distances


def main():
    queries = int(input())
    for _ in range(queries):
        nodes, edges = [int(x) for x in input().split()]
        graph = [[] for _ in range(nodes)]
        for _ in range(edges):
            n1, n2 = [int(x) - 1 for x in input().split()]
            graph[n1].append(n2)
            graph[n2].append(n1)
        start = int(input()) - 1
        result = bfs(graph, start)
        print(*result)


if __name__ == '__main__':
    main()
