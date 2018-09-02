#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/contacts/problem
"""

from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def __len__(self):
        return len(self.children)


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.is_word = True

    def starts_with(self, prefix) -> int:
        node = self.root
        for letter in prefix:
            node = node.children[letter]
            if node is None:
                return 0
        count = 0
        nodes = [node]
        while nodes:
            node = nodes.pop()
            if node.is_word:
                count += 1
            nodes.extend(node.children.values())
        return count


def main():
    n = int(input())
    trie = Trie()
    for _ in range(n):
        op, val = [x for x in input().split()]
        if op == "add":
            trie.add(val)
        else:
            print(trie.starts_with(val))


if __name__ == '__main__':
    main()
