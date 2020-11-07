#!/usr/bin/env pypy3
"""
Cut the Tree

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/cut-the-tree
"""
import sys

from typing import List

ROOT = 1
NO_PARENT = -1

def min_cut(tree: List[List[int]], weights: List[int]) -> int:
    visited = {ROOT}
    nodes = [(ROOT, NO_PARENT)]

    for node, _ in nodes:
        for neighbor in tree[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                nodes.append((neighbor, node))

    cumulative_costs = weights[:]

    for node, parent in reversed(nodes):
        if parent != NO_PARENT:
            cumulative_costs[parent] += cumulative_costs[node]

    total_cost = sum(weights)
    return min(abs(cost * 2 - total_cost) for cost in cumulative_costs)


def main():
    vertex_count = int(input())
    edge_count = vertex_count - 1
    weights = [int(x) for x in input().split()]
    tree = [[] for _ in range(vertex_count)]
    for _ in range(edge_count):
        v1, v2 = [int(x) for x in input().split()]
        v1 -= 1
        v2 -= 1
        tree[v1].append(v2)
        tree[v2].append(v1)
    cost = min_cut(tree, weights)
    print(cost)


if __name__ == "__main__":
    main()
