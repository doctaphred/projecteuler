# -*- coding: utf-8 -*-
from datetime import timedelta
from pkgutil import iter_modules
from operator import attrgetter
from functools import wraps
from datetime import datetime

from . import problems


def submodules(package):
    """Import and yield submodules within the given package."""
    for module_loader, name, ispkg in iter_modules(package.__path__):
        yield module_loader.find_module(name).load_module(name)


def timed(func):
    """Make func also return its execution time and any exception raised.

    The return value of the wrapped function is a 3-tuple:
    (result, time, exception), where:
        - result is the returned value of the function (or None if
          an exception was raised),
        - time is the time spent in the function call,
        - exception is any exception raised, or None if the function
          returned normally.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            result = None
            exception = e
        else:
            exception = None
        end = datetime.now()
        return result, end - start, exception
    return wrapper


class Problem:
    """Represents a single Project Euler problem and its solution.

    Attributes:
        number: the Project Euler problem number
        answer: the correct answer to the problem
        solution: a callable which attempts to calculate the answer
        response: the result of calling solution
        time: the time required to calculate the solution
        exception: any exception raised while calculating the solution
    """

    MAX_TIME = timedelta(minutes=1)

    def __init__(self, number, answer, solution):
        self.number = number
        self.answer = answer
        self.solution = solution
        self.response = None
        self.time = None
        self.exception = None

    @classmethod
    def discover(cls):
        """Yield instances created from submodules in this package.

        All submodules must define 'number' and 'solution' attributes,
        which will become the corresponding attributes of the created
        Problem instance. Submodules may also define an 'answer'
        attribute to enable solution verification.
        """
        for module in sorted(submodules(problems), key=attrgetter('number')):
            yield cls(module.number, getattr(module, 'answer', None),
                      module.solution)

    @property
    def correct(self):
        return self.exception is None and self.response == self.answer

    @property
    def fast_enough(self):
        return self.time is not None and self.time <= self.MAX_TIME

    def __bool__(self):
        return self.correct and self.fast_enough

    def solve(self):
        self.response, self.time, self.exception = timed(self.solution)()

    def __str__(self):
        if self.time is None:
            return 'Not solved yet!'
        if self:
            return ('Correct! Took {} seconds'
                    .format(self.time.total_seconds()))
        if self.correct:
            return ('Too slow! Took {} seconds'
                    .format(self.time.total_seconds()))
        if self.exception is not None:
            return ('{0.__class__.__name__}: {0}'.format(self.exception))
        return 'Incorrect! Expected {0.answer}, got {0.response}'.format(self)
