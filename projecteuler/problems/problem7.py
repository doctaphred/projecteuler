from itertools import islice

from projecteuler.problems.problem10 import primes


number = 7
target = 10001
answer = 104743


def nth_prime(n):
    return next(islice(primes(), n - 1, None))

assert nth_prime(1) == 2
assert nth_prime(6) == 13


def solution():
    return nth_prime(target)
