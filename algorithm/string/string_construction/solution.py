#!/bin/python3
"""
String Construction

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/challenges/string-construction
"""


def calc_min_cost(string: str) -> int:
    """Determine the minimum cost of a string."""
    cost = 0

    if not string:
        return 0

    characters = set()

    for char in string:
        if char not in characters:
            cost += 1
            characters.add(char)

    return cost


def main():
    """Print the minimum cost of each string."""
    string_count = int(input().strip())
    for _ in range(string_count):
        string = input().strip()
        result = calc_min_cost(string)
        print(result)


if __name__ == '__main__':
    main()
