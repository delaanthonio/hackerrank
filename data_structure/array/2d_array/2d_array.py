#!/usr/bin/env python3
"""
:author: Dela Anthonio
:hackerrank: hackerrank.com/delaanthonio
:problem: hackerrank.com/challenges/2d-array
"""


def main():
    n = 6
    arr = [[int(x) for x in input().split()] for _ in range(n)]
    max_sum = -9 * 7
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            top = i - 1
            bot = i + 1
            left = j - 1
            right = j + 1
            hour_glass_sum = 0
            hour_glass_sum += arr[top][left] + arr[top][j] + arr[top][right]
            hour_glass_sum += arr[i][j]
            hour_glass_sum += arr[bot][left] + arr[bot][j] + arr[bot][right]
            max_sum = max(max_sum, hour_glass_sum)
    print(max_sum)


if __name__ == '__main__':
    main()
