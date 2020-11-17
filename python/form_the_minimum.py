"""
Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once
(ignore duplicates).
Examples:
    minValue ({1, 3, 1})  ==> return (13)
"""


def min_value(digits):
    return int(''.join([str(item) for item in sorted(set(digits))]))
