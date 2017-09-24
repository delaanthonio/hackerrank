import pytest

from time_series_queries import Query, Stock, time_series_queries


@pytest.mark.parametrize("stocks, queries, results", [([
    Stock(x, y) for x, y in [(1, 5), (2, 3), (4, 12), (8, 1), (10, 10)]
], [Query(x, y) for x, y in [(1, 10), (1, 4), (2, 8), (2, 3), (1, 13)]],
                                                       [4, 1, 10, 12, -1])])
def test_time_series_queries(stocks, queries, results):
    assert time_series_queries(stocks, queries) == results
