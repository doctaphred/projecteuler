#!/usr/bin/env python3 -u
# -*- coding: utf-8 -*-
"""
Project Euler: Problem 98
=========================

https://projecteuler.net/problem=98

Anagramic squares
-----------------
By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 36 ** 2. What is
remarkable is that, by using the same digital substitutions, the
anagram, RACE, also forms a square number: 9216 = 96 ** 2. We shall call
CARE (and RACE) a square anagram word pair and specify further that
leading zeroes are not permitted, neither may a different letter have
the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text
file containing nearly two-thousand common English words, find all the
square anagram word pairs (a palindromic word is NOT considered to be an
anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""
from collections import Counter
from itertools import combinations


with open('p098_words.txt') as f:
    words = f.read().replace('"', '').split(',')


def divvy(iterable, predicate):
    """Divvy up an iterable into a dict of sets.

    >>> remainders = divvy(range(10), lambda x: x % 3)
    >>> for remainder, divisors in sorted(remainders.items()):
    ...     print(remainder, sorted(divisors))
    0 [0, 3, 6, 9]
    1 [1, 4, 7]
    2 [2, 5, 8]
    """
    results = {}
    for item in iterable:
        result = predicate(item)
        if result not in results:
            results[result] = set()
        results[result].add(item)
    return results


def letterbag(word):
    return frozenset(Counter(word).items())


anagrams = divvy(words, letterbag)
# actual_anagrams = {k: v for k, v in anagrams.items() if len(v) > 1}
# >>> sum(len(v) for v in actual_anagrams.values())
# 85
# >>> 5 Counter(len(v) for v in anagrams.values())
# Counter({1: 1701, 2: 41, 3: 1})
# >>> sum(1 for _ in anagram_pairs())
# 44


def anagram_pairs():
    for bag, matching_words in anagrams.items():
        for pair in combinations(matching_words, 2):
            # Bags with < 2 words are already excluded by combinations
            yield pair

# TODO: finish
