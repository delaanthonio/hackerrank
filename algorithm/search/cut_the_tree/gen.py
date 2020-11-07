#!/usr/bin/env pypy3
import argparse
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('seed', type=int)
    args = parser.parse_args()
    seed = args.seed

    random.seed(seed)

    MAX_NODES = 1001

    vertex_count = random.randint(3, 50)
    edge_count = vertex_count - 1
    print(vertex_count)
    weights = [random.randint(1, 100) for _ in range(min(vertex_count, MAX_NODES))]
    print(*weights)
    vertices = {x for x in range(1, vertex_count + 1)}
    queue = [vertices.pop()]
    while edge_count > 0:
        verticies_to_add_count = random.randint(1, edge_count)
        vertices_to_add = [vertices.pop() for _ in range(verticies_to_add_count)]
        for v in vertices_to_add:
            print(queue[-1], v)
        queue.extend(vertices_to_add)
        edge_count -= verticies_to_add_count


if __name__ == "__main__":
    main()
