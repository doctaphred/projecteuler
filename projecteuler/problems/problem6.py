# -*- coding: utf-8 -*-
"""
Project Euler: Problem 6
========================

https://projecteuler.net/problem=6

Sum square difference
---------------------
The sum of the squares of the first ten natural numbers is,

    12 + 22 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)**2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""
number = 6
target = 100
answer = 25164150


def sum_of_squares(n):
    return sum(n ** 2 for n in range(1, n + 1))

assert sum_of_squares(10) == 385


def square_of_sum(n):
    return sum(range(1, n + 1)) ** 2

assert square_of_sum(10) == 3025


def square_diff(n):
    return square_of_sum(n) - sum_of_squares(n)


def solution():
    return square_diff(target)
