#!/usr/bin/env python3 -u
# -*- coding: utf-8 -*-
"""
Project Euler: Problem 3
========================

https://projecteuler.net/problem=3

Largest prime factor
--------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
from projecteuler.problems.problem10 import primes


number = 3
target = 600851475143
answer = 6857


def prime_factors(n):
    sqrt_n = n ** 0.5
    for p in primes():
        if p > sqrt_n:
            return
        if not n % p:
            yield p


def solution():
    return max(prime_factors(target))


if __name__ == '__main__':
    print(solution())
