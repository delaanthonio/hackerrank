#!/usr/bin/env python3
"""
Maximizing XOR

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/maximizing-xor
"""


def max_xor(l: int, r: int) -> int:
    max_differing_bit = 0
    bit = 0
    val = 1
    while val <= r:
        val = 1 << bit
        if l & val != r & val:
            max_differing_bit = bit
        bit += 1

    return 2**(max_differing_bit + 1) - 1


def main():
    l = int(input())
    r = int(input())
    val = max_xor(l, r)
    print(val)


if __name__ == '__main__':
    main()
