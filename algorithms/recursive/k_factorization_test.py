import pytest

from k_factorization import k_factorize


@pytest.mark.parametrize("n, factors, result",
                         [(12, [2, 3, 4], [1, 3, 12]), (15, [2, 10, 6, 9, 11],
                                                        [-1]),
                          (72, [2, 4, 6, 9, 3, 7, 16, 10, 5], [1, 2, 8, 72])])
def test_trader_profit(n, factors, result):
    assert k_factorize(n, factors) == result
