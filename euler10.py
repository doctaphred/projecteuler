#!/usr/bin/env python3 -u
# -*- coding: utf-8 -*-
"""
Project Euler: Problem 10
=========================

https://projecteuler.net/problem=10

Summation of primes
-------------------
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from collections import defaultdict
from itertools import count, islice, takewhile


def primes():
    """Yield prime numbers, starting with 2.

    Algorithm by David Eppstein:
    http://code.activestate.com/recipes/117119/
    """
    # Map composites to primes witnessing their compositeness.
    composites = defaultdict(list)
    for n in count(2):
        if n not in composites:
            # n is prime
            yield n
            # Record n as a divisor of its square
            composites[n ** 2].append(n)
        else:
            # n is composite
            # Move each witness to its next multiple
            for prime_divisor in composites[n]:
                composites[prime_divisor + n].append(prime_divisor)
            # We won't see n again; free this memory
            del composites[n]


def test_primes():
    assert list(islice(primes(), 10)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def sum_of_primes_below(n):
    """Return the sum of all prime numbers < n."""
    return sum(takewhile(n.__gt__, primes()))


def test_sum_of_primes_below():
    assert sum_of_primes_below(2e6) == 142913828922


if __name__ == '__main__':
    print(sum_of_primes_below(2e6))
