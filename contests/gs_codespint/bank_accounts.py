#!/usr/bin/env python3
"""Solution for: https://www.hackerrank.com/contests/gs-codesprint/challenges/bank-accounts """

from typing import List


def fee_or_upfront(payments: List[int],
                   min_fee: int,
                   rate: float,
                   upfront_fee: int) -> str:
    """Calculate whether it's cheaper to pay all fees or pay upfront."""
    total_fee = 0
    for payment in payments:
        total_fee += max(min_fee, rate * payment)
    if total_fee <= upfront_fee:
        return "fee"
    return "upfront"


def main():
    """Print Whether it's cheaper to pay all fees or upfront for each test case."""
    test_cases = int(input().strip())
    for _ in range(test_cases):
        _, min_fee, rate, upfront_fee = [
            int(x) for x in input().strip().split()
        ]
        rate /= 100
        payments = [int(x) for x in input().strip().split()]
        result = fee_or_upfront(payments, min_fee, rate, upfront_fee)
        print(result)


if __name__ == '__main__':
    main()
