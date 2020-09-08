#!/usr/bin/env python3
"""
Super Maximum Cost Queries

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/maximum-cost-queries
"""


class UnionFind(object):
    def __init__(self, size):
        self._parents = {i: i for i in range(1, size + 1)}
        self._ranks = {i: 1 for i in range(1, size + 1)}

    def __len__(self):
        return len(self._ranks)

    def union(self, pid: int, pid2: int) -> None:
        root1 = self.find(pid)
        root2 = self.find(pid2)
        if root1 == root2:
            return
        if self._ranks[root1] >= self._ranks[root2]:
            greater = root1
            lesser = root2
        else:
            greater = root2
            lesser = root1
        self._ranks[greater] += self._ranks[lesser]
        self._parents[lesser] = self._parents[greater]

    def find(self, node: int) -> int:
        parent = self._parents[node]
        while not parent == self._parents[parent]:
            tmp_parent = self._parents[parent]
            parent = self._parents[tmp_parent]
        self._parents[node] = parent
        return parent

    def rank(self, node: int) -> int:
        return self._ranks[node]


def func() -> int:
    pass


def main():
    n = int(input())


if __name__ == '__main__':
    main()
