# -*- coding: utf-8 -*-
"""
Project Euler: Problem 5
========================

https://projecteuler.net/problem=5

Smallest multiple
-----------------
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""
from functools import reduce
from operator import mul
from math import gcd

import pytest

from projecteuler.problems.problem10 import primes


number = 5
answer = 232792560


def product(numbers):
    """Find the product of the sequence of numbers."""
    return reduce(mul, numbers, 1)


def _lcm(a, b):
    return abs(a * b) // gcd(a, b)


def lcm(numbers):
    """Find the least common multiple of the sequence of numbers."""
    return reduce(_lcm, numbers, 1)


def test_lcm():
    numbers = range(1, 21)
    n = lcm(numbers)
    assert not any(n % i for i in numbers)


def first_factor(n):
    """Find the smallest positive integer that evenly divides n."""
    sqrt_n = n ** 0.5
    for p in primes():
        if p > sqrt_n:
            # n must be prime
            return n
        if not n % p:
            return p


def factorize(n):
    """Generate prime factors of n in increasing order.

    Includes duplicate factors.

    If n is prime, yields n.
    """
    while n > 1:
        f = first_factor(n)
        yield f
        n //= f


@pytest.mark.parametrize('n, factors', [
    (0, []),
    (1, []),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (5, [5]),
    (6, [2, 3]),
    (7, [7]),
    (8, [2, 2, 2]),
    (9, [3, 3]),
    (10, [2, 5]),
    (15485863, [15485863]),
    ])
def test_factorize(n, factors):
    assert list(factorize(n)) == factors


def solution():
    return lcm(range(1, 21))
