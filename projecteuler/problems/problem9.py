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
