"""Test solution"""

from solution import sort_arr


def test_impossible_trivial():
    """Test a trivial case where the array cannot be sorted."""
    assert sort_arr([3, 1, 2]) == ()


def test_advanced_trivial():
    """Test an advanced case where the array cannot be sorted."""
    assert sort_arr([43, 65, 1, 98, 99, 101]) == ()


def test_impossible_basic():
    """Test a basic case where the array cannot be sorted."""
    assert sort_arr([3, 1, 2]) == ()


def test_swap_trivial():
    """Test a trivial case where the array can be swapped."""
    assert sort_arr([4, 2]) == ("swap", 1, 2)


def test_swap_basic2():
    """Test a basic case where two items must be swapped."""
    assert sort_arr([1, 3, 2]) == ("swap", 2, 3)


def test_swap_advanced():
    """Test a advanced case where two items must be swapped."""
    assert sort_arr([2, 5, 4, 6]) == ("swap", 2, 3)


def test_swap_basic():
    """Test a basic case where two items must be swapped."""
    assert sort_arr([1, 2, 4, 3, 5, 6]) == ("swap", 3, 4)


def test_reverse_basic():
    """Test a basic case where part of the array can be reversed."""
    assert sort_arr([1, 5, 4, 3, 2, 6]) == ("reverse", 2, 5)
