"""Tests for once in a tram."""

import once_in_a_tram as oiat


def test_digit_sum():
    assert oiat.digit_sum(357) == 15


def test_next_lucky_number():
    assert oiat.next_lucky_number(555555) == 555564
    assert oiat.next_lucky_number(555554) == 555555
    assert oiat.next_lucky_number(165901) == 165903
    assert oiat.next_lucky_number(100999) == 101002
