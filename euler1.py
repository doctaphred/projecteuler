#!/usr/bin/env python3 -u
# -*- coding: utf-8 -*-
"""
Project Euler: Problem 1
========================

https://projecteuler.net/problem=1

Multiples of 3 and 5
--------------------
If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import pytest


def sum_of_multiples_of_three_or_five_less_than(n):
    """Return the sum of all multiples of 3 or 5 below n."""
    return sum(x for x in range(n) if not x % 3 or not x % 5)


@pytest.mark.parametrize('test_input, expected', [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 3),
    (5, 3),
    (6, 8),
    (7, 14),
    (8, 14),
    (9, 14),
    (10, 23),
    (1000, 233168),
    ])
def test_sum_of_multiples_of_three_or_five_less_than(test_input, expected):
    assert sum_of_multiples_of_three_or_five_less_than(test_input) == expected


if __name__ == '__main__':
    print(sum_of_multiples_of_three_or_five_less_than(1000))
