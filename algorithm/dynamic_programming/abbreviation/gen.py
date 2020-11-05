#!/usr/bin/env pypy3
import argparse
import random

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

def main():
    parser = argparse.ArgumentParser(description='Generate random numbers.')
    parser.add_argument('seed', metavar='seed', type=int, nargs='?',
                    help='Seed', default=1)

    args = parser.parse_args()
    seed = args.seed
    random.seed(seed)

    queries = random.randint(1, 10)
    print(queries)
    for _ in range(queries):
        a = random_string_generator(6, "abAB")
        b = random_string_generator(4, "AB")
        print(a)
        print(b)

if __name__ == "__main__":
    main()
