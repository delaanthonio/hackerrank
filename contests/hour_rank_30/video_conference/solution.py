#!/usr/bin/env python3
"""
Video Conference

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/hourrank-30/challenges/video-conference
"""

from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

    def __len__(self):
        return len(self.children)


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str) -> str:
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.count += 1

    def shortest_prefix(self, word: str) -> str:
        node = self.root
        prefix = []
        for letter in word:
            prefix.append(letter)
            if letter not in node.children:
                return "".join(prefix)
            node = node.children[letter]
        if not node.count:
            return word
        return "{} {}".format(word, node.count + 1)


def main():
    n = int(input())
    trie = Trie()
    for _ in range(n):
        word = input()
        print(trie.shortest_prefix(word))
        trie.add(word)


if __name__ == '__main__':
    main()
