#!/usr/bin/env python3
"""
:author: Dela Anthonio
:hackerrank: hackerrank.com/delaanthonio
:problem:
"""

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        score_diff = b.score - a.score
        if score_diff:
            return score_diff
        return int(a.name < b.name) * -1
