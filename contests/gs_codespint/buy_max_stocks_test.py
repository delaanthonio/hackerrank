import pytest

from buy_max_stocks import buy_max_stocks


@pytest.mark.parametrize("dollars, stock_prices, max_stocks", [(45, [10, 7, 19],
                                                                4)])
def test_buy_max_stocks(dollars, stock_prices, max_stocks):
    assert buy_max_stocks(dollars, stock_prices) == max_stocks
