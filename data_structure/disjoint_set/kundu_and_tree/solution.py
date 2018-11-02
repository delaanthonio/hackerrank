#!/usr/bin/env python3
"""
Kundu and Tree

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/kundu-and-tree
"""

from math import factorial
from typing import Iterable

MOD = 10**9 + 7


class UnionFind(object):
    def __init__(self, size):
        self._parents = {i: i for i in range(1, size + 1)}
        self._ranks = {i: 1 for i in range(1, size + 1)}

    def __len__(self):
        return len(self._ranks)

    def roots(self) -> Iterable[int]:
        for p in self._parents:
            if p == self._parents[p]:
                yield p

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

    def count_triplets(self) -> int:
        triplets = combos(len(self), 3)
        for root in self.roots():
            size = self._ranks[root]
            triplets -= (len(self) - size) * combos(size, 2)
            triplets -= combos(size, 3)
        return triplets


def combos(pool: int, amount: int) -> int:
    if pool < amount:
        return 0
    count = factorial(pool)
    count = count // factorial(pool - amount)
    count = count // factorial(amount)
    return count


def main():
    n = int(input())
    uf = UnionFind(n)
    for _ in range(n - 1):
        src, dst, color = input().split()
        if color == "b":
            uf.union(int(src), int(dst))
    triplets = uf.count_triplets()
    print(triplets % MOD)


if __name__ == '__main__':
    main()
