import pytest

from solution import UnionFind, combos


@pytest.mark.parametrize("n, k, total", [(3, 1, 3), [5, 2, 10]])
def test_combos(n, k, total):
    assert combos(n, k) == total


def test_count_triplets():
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(3, 5)
    uf.union(3, 6)
    expected = combos(len(uf), 3)
    expected -= (len(uf) - 2) * combos(2, 2)
    expected -= (len(uf) - 4) * combos(4, 2)
    expected -= combos(4, 3)
    assert (uf.count_triplets()) == expected
