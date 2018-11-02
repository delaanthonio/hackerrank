#!/usr/bin/env python3
""" Solution for https://www.hackerrank.com/challenges/almost-sorted
    Given an array with  elements, can you sort this array in ascending order using
    only one of the following operations?
"""

from typing import List, Tuple


def sort_arr(arr: List[int]) -> Tuple[str, int, int]:
    """Determine if an array can be sorted."""
    # Trivial case
    if len(arr) == 2:
        return ("swap", 1, 2)

    inversions = []

    for i, (x, y) in enumerate(zip(arr, arr[1:]), start=1):
        if x > y:
            inversions.append(i)

    output_start = inversions[0]
    output_end = inversions[-1] + 1

    first_inv = inversions[0] - 1
    last_inv = inversions[-1]

    if len(inversions) <= 2:
        if last_inv < len(arr) - 1 and arr[first_inv] > arr[last_inv + 1]:
            return ()
        if first_inv is not 0 and arr[first_inv - 1] > arr[last_inv]:
            return ()
        return ("swap", output_start, output_end)

    if arr[last_inv] > arr[first_inv - 1]:
        if arr[first_inv] < arr[last_inv + 1] and all(
                x + 1 == y for x, y in zip(inversions, inversions[1:])):
            return ("reverse", output_start, output_end)
    return ()


def main() -> None:
    """Print if array can be sorted"""
    _ = int(input().strip())
    arr = [int(x) for x in input().strip().split(' ')]
    result = sort_arr(arr)
    if result:
        print("yes")
        operation, start, end = result
        print("{} {} {}".format(operation, start, end))
    else:
        print("no")


if __name__ == '__main__':
    main()
