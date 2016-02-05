# -*- coding: utf-8 -*-
import sys

from .problem import Problem


def main():
    problems = list(Problem.discover())

    if not problems:
        print('Did not find any problems!')
        sys.exit(1)

    num_problems = len(problems)

    if num_problems == 1:
        print('1 problem attempted')
    else:
        print(num_problems, 'problems attempted')

    for i, problem in enumerate(problems, start=1):
        print()
        print('{}/{}: Solving problem {}...'
              .format(i, num_problems, problem.number))
        problem.solve()
        print(problem)

    print()
    total_seconds = sum(problem.time.total_seconds() for problem in problems)
    print(total_seconds, 'seconds total')
    num_correct = sum(problem.correct for problem in problems)
    print('{}/{} correct'.format(num_correct, num_problems))

    if num_correct == num_problems:
        print('You win!')
    else:
        print('FAILURE')
        sys.exit(1)


if __name__ == '__main__':
    main()
