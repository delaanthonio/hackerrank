#!/usr/bin/env python3
"""Solution for https://www.hackerrank.com/challenges/even-tree"""

from collections import defaultdict, deque
from typing import Dict, Set

Vertex = int
Tree = Dict[Vertex, Set[Vertex]]


def trim_tree(tree: Tree, root=1) -> None:
    """Make tree a directed graph."""
    for child in tree[root]:
        try:
            tree[child].remove(root)
        except KeyError:
            pass
        trim_tree(tree, child)


def prune_tree(tree: Tree, root: Vertex=1) -> int:
    """Given a tree, determine the amount of edges that can be pruned."""
    count = 0
    for child in tree[root]:
        if tree_size(tree, child) % 2 == 0:
            count += 1
        count += prune_tree(tree, child)

    return count


def tree_size(subtree: Tree, start: Vertex=1, *, root: Vertex=1) -> int:
    """Count the amount of vertices in the subtree using a bfs traversal."""
    visited = {root, start}
    queue = deque([x for x in subtree[start]])
    count = 1
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            count += 1
            for next_vertex in subtree[vertex]:
                if next_vertex not in visited:
                    queue.append(next_vertex)
    return count


def main():
    """Print the amount of edges that can be pruned from a tree."""
    tree = defaultdict(set)
    vertex_count, edge_count = input().split()
    vertex_count = int(vertex_count)
    edge_count = int(edge_count)
    for _ in range(edge_count):
        v1, v2 = input().split()
        v1 = int(v1)
        v2 = int(v2)
        tree[v1].add(v2)
        tree[v2].add(v1)
    trim_tree(tree)
    print(prune_tree(tree))


if __name__ == '__main__':
    main()
