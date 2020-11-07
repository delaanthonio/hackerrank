#!/usr/bin/env pypy3
"""
Cut the Tree

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/cut-the-tree
"""
import sys


def dfs(graph, weights, seen, start) -> int:
    queue = [start]
    cost = 0
    while queue:
        node = queue.pop()
        cost += weights[node]
        for n in graph[node]:
            if n in seen:
                continue
            seen.add(n)
            queue.append(n)
    return cost


def min_cost(graph, weights) -> int:
    cost = 10 ** 5
    for vertex, neighbors in enumerate(graph):
        for n in neighbors:
            cost1 = dfs(graph, weights, {vertex, n}, n)
            cost2 = dfs(graph, weights, {vertex, n}, vertex)
            cost = min(abs(cost1 - cost2), cost)
    return cost


def main():
    vertex_count = int(input())
    edge_count = vertex_count - 1
    weights = [int(x) for x in input().split()]
    graph = [[] for _ in range(vertex_count)]
    for _ in range(edge_count):
        v1, v2 = [int(x) for x in input().split()]
        v1 -= 1
        v2 -= 1
        graph[v1].append(v2)
        graph[v2].append(v1)
    cost = min_cost(graph, weights)
    print(cost)


if __name__ == "__main__":
    main()
