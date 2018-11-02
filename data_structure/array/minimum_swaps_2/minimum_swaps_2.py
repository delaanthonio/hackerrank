#!/usr/bin/env python3
"""
:problem: https://www.hackerrank.com/challenges/minimum-swaps-2/problem
"""


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    sorted_arr = sorted(arr)
    swaps = 0
    expected_indicies = {val: i for i, val in enumerate(sorted_arr)}
    for i, (val, expected_val) in enumerate(zip(arr, sorted_arr)):
        while not val == expected_val:
            expected_index = expected_indicies[val]
            arr[i], arr[expected_index] = arr[expected_index], arr[i]
            val = arr[i]
            swaps += 1
    print(swaps)


if __name__ == '__main__':
    main()
