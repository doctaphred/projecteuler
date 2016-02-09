from functools import reduce
from operator import mul
from math import gcd

import pytest

from projecteuler.problems.problem10 import primes


number = 5
answer = 232792560


def product(numbers):
    return reduce(mul, numbers, 1)


def _lcm(a, b):
    return abs(a * b) // gcd(a, b)


def lcm(numbers):
    return reduce(_lcm, numbers, 1)


def test_lcm():
    numbers = range(1, 21)
    n = lcm(numbers)
    assert not any(n % i for i in numbers)


def first_factor(n):
    sqrt_n = n ** 0.5
    for p in primes():
        if p > sqrt_n:
            # n must be prime
            return n
        if not n % p:
            return p


def factorize(n):
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
