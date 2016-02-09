from itertools import combinations_with_replacement

import pytest


def palindromic(n):
    n = str(n)
    # reversed(n) returns a reversed iterator; use slicing instead
    return n == n[::-1]


@pytest.mark.parametrize('n', [
    1,
    101,
    1001,
    10101,
    1234567890987654321,
    ])
def test_palindromic(n):
    assert palindromic(n)


@pytest.mark.parametrize('n', [
    10,
    100,
    12345678900987654320,
    ])
def test_not_palendromic(n):
    assert not palindromic(n)


number = 4
answer = 906609


def three_digit_products():
    for i, j in combinations_with_replacement(range(100, 1000), 2):
        yield i * j


def solution():
    return max(n for n in three_digit_products() if palindromic(n))
