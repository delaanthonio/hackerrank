import pytest

from solution import count_ways


@pytest.mark.parametrize("args, ways", [([4, 3, 2], 3), ([3, 2, 1], 1),
                                        ([4, 4, 2], 7), ([5, 4, 2], 20)])
def test_min_travel_distance(args, ways):
    assert count_ways(*args) == ways
