# -*- coding: utf-8 -*-
"""
Project Euler: Problem 9
========================

https://projecteuler.net/problem=9

Special Pythagorean triplet
---------------------------
A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which, a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from itertools import combinations


number = 9
target = 1000
answer = 31875000


def whatever(n):
    for a, b in combinations(range(1, n), 2):
        c = n - a - b
        if a ** 2 + b ** 2 == c ** 2:
            yield a * b * c


def solution():
    return next(whatever(target))
