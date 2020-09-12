#!/usr/bin/env python3
"""
Balanced Forest

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/balanced-forest
"""

import sys
from typing import Iterable, List, Set, Tuple

Edge = Tuple[int, int]


class Tree(object):
    def __init__(self, node_count, edges, costs):
        self.children = [set() for _ in range(node_count)]
        self.costs = costs
        for edge in edges:
            self.add_edge(*edge)

    def __getitem__(self, node):
        return self.children[node]

    def __len__(self):
        return len(self.children)

    def __iter__(self):
        return iter(range(len(self)))

    def subtree_cost(self, start: int, seen: Set[int]) -> int:
        nodes = [start]
        cost = 0
        while nodes:
            node = nodes.pop()
            if node not in seen:
                seen.add(node)
                cost += self.costs[node]
                for neighbor in self[node]:
                    nodes.append(neighbor)
        return cost

    def add_edge(self, src: int, dest: int):
        self[src].add(dest)
        self[dest].add(src)

    def remove_edge(self, src: int, dest: int):
        self[src].remove(dest)
        self[dest].remove(src)

    def subtree_costs(self, e1: Edge, e2: Edge) -> List[int]:
        seen = set()
        costs = []

        self.remove_edge(*e1)
        self.remove_edge(*e2)

        for node in self:
            if node not in seen:
                costs.append(self.subtree_cost(node, seen))

        self.add_edge(*e1)
        self.add_edge(*e2)

        return sorted(costs)

    def balance(self, edges: List[Edge]) -> Iterable[int]:
        for e1 in reversed(edges):
            edges.pop()
            for e2 in edges:
                costs = self.subtree_costs(e1, e2)
                if len(costs) >= 2 and costs[-2] == costs[-1]:
                    print(costs, file=sys.stderr)
                    yield costs[-1] - costs[0]


def main():
    queries = int(input())
    for _ in range(queries):
        node_count = int(input())
        costs = [0] + [int(x) for x in input().split()]
        edges = []
        for _ in range(node_count - 1):
            edge = tuple(int(x) for x in input().split())
            edges.append(edge)
        edges.append((0, 1))  # Dummy edge
        tree = Tree(node_count + 1, edges, costs)
        costs = [x for x in tree.balance(edges)]
        print(min(costs) if costs else -1)


if __name__ == '__main__':
    main()
