import pytest

from solution import min_avg_time


@pytest.mark.parametrize("orders, time", [([(0, 3), (1, 9), (2, 6)], 9),
                                          ([(0, 10), (10, 2)], 6),
                                          ([(0, 5), (2, 3), (1, 4)], 7)])
def test_min_avg_wait_time(orders, time):
    # import pdb
    # pdb.set_trace()
    assert min_avg_time(orders) == time
