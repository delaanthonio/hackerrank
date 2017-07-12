#!/usr/bin/env python3
"""Solution for https://www.hackerrank.com/challenges/fibonacci-modified"""

import functools as ft


@ft.lru_cache()
def mod_fib(t1: int, t2: int, num: int) -> int:
    """Calculate tn."""
    if num == 1:
        return t1
    if num == 2:
        return t2
    return mod_fib(num - 2, t1, t2) + mod_fib(num - 1, t1, t2)**2


def main() -> None:
    """Given t1, t2, and n, print tn."""
    t1, t2, num = input().split()
    t1, t2, num = int(t1), int(t2), int(num)
    print(mod_fib(t1, t2, num))


if __name__ == '__main__':
    main()
