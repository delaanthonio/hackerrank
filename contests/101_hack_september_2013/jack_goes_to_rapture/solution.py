#!/usr/bin/env pypy3
"""
Jack goes to Rapture

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/101sep13/challenges/jack-goes-to-rapture
"""

import heapq
import sys

def shortest_path(graph, node_count, start, target):
    nodes = [(1, start)]
    visited = [False] * node_count
    node = start

    while nodes and node != target:
        weight, node = heapq.heappop(nodes)
        visited[node] = True
        for neighbor, neighbor_weight in graph[node]:
            if visited[neighbor]:
                continue
            heapq.heappush(nodes, (max(neighbor_weight, weight), neighbor))
    
    return node == target, weight


def main():
    node_count, edge_counnt = [int(x) for x in input().split()]
    graph = []
    for _ in range(node_count):
        graph.append([])
    for _ in range(edge_counnt):
        src, dest, weight = [int(x) for x in input().split()]
        src -= 1
        dest -= 1
        graph[src].append((dest, weight))
        graph[dest].append((src, weight))

    found, weight = shortest_path(graph, node_count, 0, node_count - 1)
    print(weight if found else "NO PATH EXISTS")


if __name__ == "__main__":
    main()
