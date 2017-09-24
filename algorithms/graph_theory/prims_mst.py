#!/usr/bin/env python3
"""Solution for: https://www.hackerrank.com/challenges/primsmstsub
"""

from collections import defaultdict, namedtuple
from queue import PriorityQueue
from typing import Dict, List

Edge = namedtuple("Edge", ['weight', 'src', 'dest'])
Graph = Dict[int, List[Edge]]


def prims_mst(graph: Graph, start: int) -> List[Edge]:
    """Calculate the minimum spanning tree of a given graph."""
    mst = []
    visited = {0}
    edge_candidates = PriorityQueue()
    next_vertex = start

    for _ in range(len(graph) - 1):
        visited.add(next_vertex)
        for edge in graph[next_vertex]:
            if edge.dest not in visited:
                edge_candidates.put(edge)
        candidate = edge_candidates.get()  # type: Edge
        while candidate.dest in visited:
            candidate = edge_candidates.get()
        next_vertex = candidate.dest
        mst.append(candidate)

    return mst


def main():
    """Print the total weight of the smallest minimum spanning tree."""
    n, m = [int(x) for x in input().split()]
    graph = defaultdict(list)
    for _ in range(m):
        v1, v2, w = [int(x) for x in input().split()]  # type: Edge
        graph[v1].append(Edge(src=v1, dest=v2, weight=w))
        graph[v2].append(Edge(src=v2, dest=v1, weight=w))
    start = int(input().strip())
    print(sum(x.weight for x in prims_mst(graph, start)))


if __name__ == '__main__':
    main()
