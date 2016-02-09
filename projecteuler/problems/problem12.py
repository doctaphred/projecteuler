from collections import Counter
from itertools import count, islice

from projecteuler.problems.problem5 import factorize


number = 12
target = 500
answer = 76576500


def triangle_numbers():
    current = 0
    for i in count(1):
        current += i
        yield current

assert list(islice(triangle_numbers(), 10)) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]


def num_divisors(n):
    c = Counter(factorize(n))
    total = 1
    for n in c.values():
        total *= n + 1
    return total


divisor_tests = {
    1: [1],
    3: [1, 3],
    6: [1, 2, 3, 6],
    10: [1, 2, 5, 10],
    15: [1, 3, 5, 15],
    21: [1, 3, 7, 21],
    28: [1, 2, 4, 7, 14, 28],
}

for k, expected in divisor_tests.items():
    assert num_divisors(k) == len(expected)


def solution():
    return next(n for n in triangle_numbers() if num_divisors(n) > target)
