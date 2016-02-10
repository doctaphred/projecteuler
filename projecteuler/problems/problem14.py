# -*- coding: utf-8 -*-
"""
Project Euler: Problem 14
=========================

https://projecteuler.net/problem=10

Longest Collatz sequence
------------------------
The following iterative sequence is defined for the set of positive
integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz
Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one
million.
"""
from functools import lru_cache


number = 14
target = 1000000
answer = 837799


@lru_cache(target * 2)
def collatz(n):
    if n == 1:
        return [n]
    elif n % 2:
        return [n] + collatz(3 * n + 1)
    else:
        return [n] + collatz(n // 2)

assert collatz(1) == [1]
assert collatz(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


@lru_cache(target * 2)
def collatz_len(n):
    if n == 1:
        return 1
    elif n % 2:
        return 1 + collatz_len(3 * n + 1)
    else:
        return 1 + collatz_len(n // 2)

assert collatz_len(1) == 1
assert collatz_len(13) == 10


def solution():
    return max(range(1, target), key=collatz_len)
