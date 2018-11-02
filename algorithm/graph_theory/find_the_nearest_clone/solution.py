#!/usr/bin/env python3
"""
Find the nearest clone

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/find-the-nearest-clone
"""

from collections import defaultdict, deque
from typing import Iterable, Optional, Set


class Graph(object):
    def __init__(self, edges, colors):
        self.nodes = defaultdict(list)
        self.colors = {i: color for i, color in enumerate(colors, start=1)}
        for src, dest in edges:
            self.add_edge(src, dest)

    def add_edge(self, src: int, dest: int):
        self.nodes[src].append(dest)
        self.nodes[dest].append(src)

    def _shortest_path(self, color: int) -> Iterable[int]:
        seen = set()
        for n, c in self.colors.items():
            if color == c:
                yield self.color_bfs(n, color, seen)

    def shortest_path(self, color: int) -> int:
        distances = [x for x in self._shortest_path(color) if x]
        return min(distances) if distances else -1

    def color_bfs(self, node: int, color: int,
                  seen: Set[int]) -> Optional[int]:
        nodes = deque(self.nodes[node])
        seen.add(node)
        distances = {n: 1 for n in nodes}
        while nodes:
            n = nodes.popleft()
            if n in seen:
                continue
            seen.add(n)
            if self.colors[n] == color:
                return distances[n]
            nodes.extend(self.nodes[n])
            distances.update((adj, distances[n] + 1) for adj in self.nodes[n])
        return None


def main():
    n, e = [int(x) for x in input().split()]
    edges = []
    for _ in range(e):
        edge = [int(x) for x in input().split()]
        edges.append(edge)
    colors = [int(x) for x in input().split()]
    graph = Graph(edges, colors)
    target_color = int(input())
    distance = graph.shortest_path(target_color)
    print(distance)


if __name__ == '__main__':
    main()
