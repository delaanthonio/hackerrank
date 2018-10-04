import pytest

from solution import areas


@pytest.mark.parametrize(
    "heights, area",
    [([1, 2, 3, 4, 5], 9), ([1, 5, 2], 5), ([11, 10, 11], 30),
     ([1, 4, 3, 3, 1], 9), ([1, 4, 3, 3], 9), ([8, 4, 6, 5, 7, 3], 20),
     ([8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116], 26152)])
def test_lexographical_min(heights, area):
    assert max(areas(heights)) == area
