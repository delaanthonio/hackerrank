#!/usr/bin/env python3
"""
Tree: Huffman Decoding

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/tree-huffman-decoding
"""


class Node:
    def __init__(self, freq: int, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None


def decodeHuff(root, encoded: str) -> None:
    node = root
    answer = []
    for char in encoded:
        if char == "0":
            node = node.left
        else:
            node = node.right
        if node.data != "\0":
            answer.append(node.data)
            node = root

    print("".join(answer))
