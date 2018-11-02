#!/usr/bin/py

from typing import Set


def pair_count(ints: Set[int], diff: int) -> int:
    count = 0
    for i in ints:
        if i + diff in ints:
            count += 1
    return count


if __name__ == '__main__':
    n, k = [int(x) for x in input().split()]
    b = {int(x) for x in input().split()}
    print(pair_count(b, k))
