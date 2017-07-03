#!/usr/bin/env python3
"""Solution for https://www.hackerrank.com/challenges/solve-me-first"""


def solve_me_first(num1: int, num2: int):
    """Calculate the sum of two numbers."""
    return num1 + num2


def main():
    """Print the sum of two numbers."""
    num1 = int(input())
    num2 = int(input())
    result = solve_me_first(num1, num2)
    print(result)


if __name__ == '__main__':
    main()
