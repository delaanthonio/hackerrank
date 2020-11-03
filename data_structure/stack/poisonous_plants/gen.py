#!/usr/bin/env pypy3
import random
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate random numbers.')
    parser.add_argument('seed', metavar='seed', type=int, nargs='?',
                    help='Seed', default=1)

    args = parser.parse_args()
    seed = args.seed
    random.seed(seed)

    length = random.randint(1, 100)
    nums = [random.randint(0, 50) for _ in range(length)]
    print(length)
    print(*nums)

if __name__ == "__main__":
    main()
