#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/bfsshortreach
"""

from collections import defaultdict, deque
from typing import List

EDGE_LENGTH = 6


def bfs(graph: List[List[int]], start: int) -> List[int]:
    distance = defaultdict(lambda: -1)
    queue = deque([start])
    visited = {start}
    rounds = 1
    staging = deque()
    while queue:
        node = queue.popleft()
        for nbr in graph[node]:
            if nbr not in visited:
                distance[nbr] = rounds * EDGE_LENGTH
                staging.append(nbr)
                visited.add(nbr)
        if not queue:
            rounds += 1
            queue, staging = staging, queue
    return [distance[i] for i in range(len(graph)) if not i == start]


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
