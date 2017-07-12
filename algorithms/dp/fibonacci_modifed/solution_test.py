"""Tests for Fibonnaci Modified."""
import solution as fib


def test_low_mod_fib():
    """Test mod_fib() with a low tn."""
    assert fib.mod_fib(0, 1, 5) == 5


def test_high_mod_fib():
    """Test mod_fib() with a high tn."""
    assert fib.mod_fib(0, 1, 10) == 84266613096281243382112
