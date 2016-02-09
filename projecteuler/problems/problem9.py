number = 9
target = 1000
answer = 31875000


def whatever(n):
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if (a + b + c == n and
                        a ** 2 + b ** 2 == c ** 2):
                    yield a * b * c


def solution():
    return next(whatever(1000))
