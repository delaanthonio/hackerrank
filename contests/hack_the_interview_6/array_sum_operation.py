#!/usr/bin/env python3
"""
Array-Sum Operation

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/hack-the-interview-vi/challenges/maximum-sum-10-1
"""


def main():
    n, m = [int(x) for x in input().split(" ")]
    nums = [x + 1 for x in range(n)]
    nums_set = {x for x in nums}
    count = sum(nums)

    for x in range(m):
        op = int(input())
        if op in nums_set:
            nums[0], nums[-1] = nums[-1], nums[0]
        else:
            count -= nums[-1]
            count += op
            nums_set.remove(nums[-1])
            nums_set.add(op)
            nums[-1] = op
        print(count)


if __name__ == "__main__":
    main()
