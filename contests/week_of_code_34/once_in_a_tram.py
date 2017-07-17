#!/usr/bin/env python3
"""Solution for https://www.hackerrank.com/contests/w34/challenges/once-in-a-tram"""


def digit_sum(num: int) -> int:
    """Calculate the sum of a number's digits."""
    total = 0
    while num:
        total, num = total + num % 10, num // 10
    return total


def next_lucky_number(num: int) -> int:
    """Calculate the next lucky number."""
    num += 1
    while True:
        left_half = num // 1000
        right_half = num % 1000
        if digit_sum(left_half) != digit_sum(right_half):
            num += 1
        else:
            break
    return left_half * 1000 + right_half


def main():
    """Print the next lucky number"""
    num = int(input().strip())
    result = next_lucky_number(num)
    print(result)


if __name__ == '__main__':
    main()
