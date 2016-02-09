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
    return square_diff(100)
