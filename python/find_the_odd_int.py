"""
Given an array, find the integer that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""


def find_it(seq):
    return [item for item in set(seq) if seq.count(item) % 2][0]
