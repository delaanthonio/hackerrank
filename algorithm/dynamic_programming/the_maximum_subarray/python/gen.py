#!/usr/bin/env pypy3
import argparse
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('seed', type=int)
    args = parser.parse_args()
    seed = args.seed

    random.seed(seed)

    queries = random.randint(1, 10)
    print(queries)
    for _ in range(queries):
        arr_len = random.randint(1, 20)
        print(arr_len)
        arr = [random.randint(-20, 20) for _ in range(arr_len)]
        print(*arr)

if __name__ == "__main__":
    main()
