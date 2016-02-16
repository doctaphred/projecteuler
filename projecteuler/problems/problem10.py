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
from itertools import count, islice, takewhile
from functools import wraps


number = 10
target = 2e6
answer = 142913828922


def reuse(gen_func):
    """Reuse a generator!"""
    history = []
    gen = gen_func()

    @wraps(gen_func)
    def reusable():
        yield from history
        for x in gen:
            history.append(x)
            yield x

    return reusable


@reuse
def primes():
    """Yield prime numbers, starting with 2.

    Algorithm by David Eppstein, Alex Martelli, and Tim Hochberg:
    http://code.activestate.com/recipes/117119/#c2
    """
    yield 2
    # Map composites to primes witnessing their compositeness
    composites = {}
    # Skip even numbers
    for n in count(3, step=2):
        # We won't see n again, so we can delete its witness, if any
        prime_divisor = composites.pop(n, None)
        if prime_divisor is None:
            # n is prime
            yield n
            # Record n as a divisor of its square
            composites[n ** 2] = 2 * n
        else:
            # n is composite
            # Move the witness to a new multiple
            x = n + prime_divisor
            while x in composites:
                x += prime_divisor
            composites[x] = prime_divisor


def test_primes():
    assert list(islice(primes(), 10)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def sum_of_primes_below(n):
    """Return the sum of all prime numbers < n."""
    return sum(takewhile(n.__gt__, primes()))


def test_sum_of_primes_below():
    assert sum_of_primes_below(target) == answer


def solution():
    return sum_of_primes_below(target)


if __name__ == '__main__':
    print(solution())
