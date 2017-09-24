import pytest

from prims_mst import Edge, defaultdict, prims_mst


@pytest.mark.parametrize("edges, start, result",
                         [([(1, 2, 3), (1, 3, 4), (4, 2, 6), (5, 2, 2),
                            (2, 3, 5), (3, 5, 7)], 1, 15)])
def test_prims_mst(edges, start, result):
    graph = defaultdict(list)
    for v1, v2, w in edges:
        graph[v1].append(Edge(src=v1, dest=v2, weight=w))
        graph[v2].append(Edge(src=v2, dest=v1, weight=w))
    assert sum(x.weight for x in prims_mst(graph, start)) == result
