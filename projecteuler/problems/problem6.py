number = 6
answer = 25164150


def sum_of_squares(n):
    return sum(n ** 2 for n in range(1, n + 1))

assert sum_of_squares(10) == 385


def square_of_sum(n):
    return sum(range(1, n + 1)) ** 2

assert square_of_sum(10) == 3025


def solution():
    return square_of_sum(100) - sum_of_squares(100)
