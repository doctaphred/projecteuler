# -*- coding: utf-8 -*-
"""
Project Euler: Problem 7
========================

https://projecteuler.net/problem=7

10001st prime
-------------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10,001st prime number?
"""
from itertools import islice

from projecteuler.problems.problem10 import primes


number = 7
target = 10001
answer = 104743


def nth_prime(n):
    """Find the nth prime number."""
    return next(islice(primes(), n - 1, None))

assert nth_prime(1) == 2
assert nth_prime(6) == 13


def solution():
    return nth_prime(target)
