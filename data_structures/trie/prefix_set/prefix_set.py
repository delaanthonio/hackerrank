#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/no-prefix-set/problem
"""

from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word) -> bool:
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.is_word = True
        return bool(node.children)

    def search(self, word) -> bool:
        node = self.root
        for letter in word:
            node = node.children[letter]
            if not node:
                return False
            if node.is_word:
                return True
        return False


def main():
    n = int(input())
    trie = Trie()
    for _ in range(n):
        word = input()
        if trie.search(word) or trie.add(word):
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")


if __name__ == '__main__':
    main()
