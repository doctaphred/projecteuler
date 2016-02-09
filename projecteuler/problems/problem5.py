from collections import Counter
from functools import reduce
from operator import mul

import pytest

from projecteuler.problems.problem10 import primes


number = 5
answer = 232792560


def product(numbers):
    return reduce(mul, numbers, 1)


def largest_factor_product(numbers):
    largest_factor_counts = Counter()
    for n in numbers:
        for factor, factor_count in Counter(factorize(n)).items():
            if factor_count > largest_factor_counts[factor]:
                largest_factor_counts[factor] = factor_count
    return product(largest_factor_counts.elements())


def test_largest_factor_product():
    numbers = range(1, 21)
    n = largest_factor_product(numbers)
    assert not any(n % i for i in numbers)


def factorize(n):
    while n > 1:
        sqrt_n = n ** 0.5
        for p in primes():
            if p > sqrt_n:
                # n must be prime
                yield n
                return
            if not n % p:
                yield p
                n //= p
                break


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
    # return next(n for n in count(1) if evenly_divisible(n))
    return largest_factor_product(range(1, 21))
