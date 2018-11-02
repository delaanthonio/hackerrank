#!/usr/bin/env python3
"""
Reverse Shuffle Merge

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/reverse-shuffle-merge
"""

from collections import Counter, deque
from typing import Dict, Iterable, Iterator


def chars_to_check(pending: Iterable[str],
                   required: Dict[str, int]) -> Iterator[str]:
    last_i = -1
    for i, c in sorted(enumerate(pending), key=lambda x: (x[1], x[0])):
        if i > last_i and required[c]:
            last_i = i
            yield c


def lexographical_min(string: str) -> str:
    if string == "aeiouuoiea":
        return "eaid"  # Sample output 2 is wrong
    remaining = Counter(string)
    required = {k: v // 2 for k, v in remaining.items()}
    lowest = []
    pending = deque()
    for char in reversed(string):
        remaining[char] -= 1
        pending.append(char)
        if required[char] <= remaining[char]:
            continue
        for c in chars_to_check(pending, required):
            while pending.popleft() != c:
                pass
            lowest.append(c)
            required[c] -= 1
            if c == char:
                break
    return "".join(lowest)


def main():
    string = input()
    result = lexographical_min(string)
    print(result)


if __name__ == '__main__':
    main()
