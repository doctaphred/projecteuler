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
from itertools import combinations, permutations
from math import isqrt
from pkg_resources import resource_string


number = 98
answer = 18769


def is_square(i):
    return isqrt(i) ** 2 == i


def divvy(predicate, iterable):
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


def charlist(word):
    return ''.join(sorted(word))


def anagram_pairs(word_list):
    keys = divvy(charlist, word_list)
    for _, words in sorted(keys.items(), key=lambda x: -len(x[0])):
        for pair in combinations(words, 2):
            # Bags with < 2 words are already excluded by combinations.
            yield pair


def translate(translation, word):
    return int(''.join(translation[char] for char in word))


def numeric_translations(chars):
    index = {char: i for i, char in enumerate(chars)}
    for digits in permutations('987654321', len(chars)):
        yield {char: digits[index[char]] for char in index}


def square_anagrams(word1, word2):
    assert word1 != word2
    assert sorted(word1) == sorted(word2)

    for translation in numeric_translations(sorted(set(word1))):
        n1 = translate(translation, word1)
        if not is_square(n1):
            continue
        n2 = translate(translation, word2)
        if not is_square(n2):
            continue
        yield n1, n2


def largest_square_anagram(word_list):
    for word1, word2 in anagram_pairs(word_list):
        for n1, n2 in square_anagrams(word1, word2):
            return max(n1, n2)


def read_words():
    return (
        resource_string('projecteuler.resources', 'p098_words.txt')
        .decode()  # By 'resource_string' it means 'bytes' -.-
        .replace('"', '')
        .split(',')
    )


def solution():
    word_list = read_words()
    return largest_square_anagram(word_list)


# def letterbag(word):
#     from collections import Counter
#     return frozenset(Counter(word).items())


# def anagrams(string):
#     seen = {string}
#     for perm in permutations(string):
#         anagram = ''.join(perm)
#         if anagram not in seen:
#             seen.add(anagram)
#             yield anagram


# def numeric_anagrams(n):
#     for anagram in anagrams(str(n)):
#         if not anagram.startswith('0'):
#             yield int(anagram)
