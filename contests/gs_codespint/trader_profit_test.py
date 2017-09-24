import pytest

from trader_profit import trader_profit


@pytest.mark.parametrize("transactions, stock_prices, expected_profit",
                         [(1, [12, 5, 10, 7, 17],
                           12), (2, [10, 22, 5, 75, 65, 80],
                                 87), (3, [20, 580, 420, 900], 1040),
                          (1, [100, 90, 80, 50, 25], 0)])
def test_trader_profit(transactions, stock_prices, expected_profit):
    assert trader_profit(transactions, stock_prices) == expected_profit
