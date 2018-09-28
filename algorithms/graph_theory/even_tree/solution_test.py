"""Test Even Tree solution"""

from solution import prune_tree, tree_size, trim_tree


def test_trivial_prune():
    """Test trivial case where no edges can be pruned."""
    graph = {1: {2}, 2: {1}}
    trim_tree(graph)
    assert tree_size(graph) == 2
    assert prune_tree(graph) == 0


def test_basic_prune():
    """Basic test case."""
    graph = {1: {2, 3}, 2: {1, 4}, 3: {1}, 4: {2}}
    trim_tree(graph)
    assert tree_size(graph) == 4
    assert prune_tree(graph) == 1


def test_sample_prune():
    """Basic test case."""
    graph = {
        1: {2, 3, 6},
        2: {1, 5, 7},
        3: {1, 4},
        4: {3},
        5: {2},
        6: {1, 8},
        7: {2},
        8: {6, 9, 10},
        9: {8},
        10: {8}
    }
    trim_tree(graph)
    assert tree_size(graph) == 10
    assert prune_tree(graph) == 2
